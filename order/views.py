from django.http import Http404
from django.shortcuts import redirect, render

from main.models import Burger

def cart_inc(request, id):
    cart_change(request, id, 1)
    print(id)
    return redirect(request.GET.get("to", "catalog:index"))


def cart_dec(request, id):
    cart_change(request, id, -1)
    return redirect(request.GET.get("to", "catalog:index"))


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
