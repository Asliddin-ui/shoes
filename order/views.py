from django.contrib.admin.templatetags import log
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from .models import OrderProduct, Order
from .forms import OrderForm
from main.models import Burger


def cart_inc(request, id):
    cart_change(request, id, 1)
    return redirect(request.GET.get("to", "main:index"))


def cart_dec(request, id):
    cart_change(request, id, -1)
    return redirect(request.GET.get("to", "main:index"))


def cart_change(request, pid, n):
    p = Burger.objects.get(id=pid)

    if p.status != Burger.STATUS_PUBLISHED or p.available == 0:
        raise Http404()

    data = request.session.get("data", {})
    sid = str(p.id)
    if sid not in data:
        data[sid] = 0

    data[sid] += n
    data[sid] = min(p.available, data[sid])
    if data[sid] <= 0:
        del data[sid]   
    request.session["data"] = data

@method_decorator(login_required(login_url=reverse_lazy('registration:login')), name='dispatch')
class CheckoutView(CreateView):
    form_class = OrderForm
    template_name = "main/checkout.html"

    def form_valid(self, form):
        if self.request.user.is_anonymous:
            print(self.request.user.is_anonymous)
            return redirect("registration:login")
        with transaction.atomic():
            data = self.request.session.get("data", {})
            burgers = []
            total_price = 0
            for k, v in data.items():
                burger = Burger.objects.select_for_update().get(id=k)
                if burger.available < v or burger.status != Burger.STATUS_PUBLISHED:
                    return redirect("order:checkout")

                burger.available -= v
                total_price += v * burger.price
                burger.save()

                burgers.append(
                    OrderProduct(burger_id=burger.id, price=burger.price, amount=v)
                )

            order = form.save(commit=False)
            order.user_id = self.request.user.id
            order.status = Order.STATUS_NEW
            order.payment_status = Order.PAYMENT_STATUS_NONE
            order.total_price = total_price
            order.save()

            for b in  burgers:
                b.order_id = order.id

            OrderProduct.objects.bulk_create(burgers)

            del self.request.session["data"]

        return redirect("main:index")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        data = self.request.session.get("data", {})
        burger = Burger.objects.filter(status=Burger.STATUS_PUBLISHED, id__in=data.keys()).all()
        total_price = 0
        for row in burger:
            row.in_cart = data.get(str(row.id), 0)
            row.total_price = row.in_cart * row.price
            total_price = row.total_price

        kwargs["burgers"] = burger
        kwargs["total_price"] = total_price

        return kwargs
    