from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from main.models import Category, Burger, WhyModel


class MainIndex(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        cat = Category.objects.filter(parent_id__isnull = False )
        cats_with_food = {}
        for c in cat:
            cats_with_food[c] = Burger.objects.filter(category=c)

        kwargs['why'] = WhyModel.objects.all().order_by('id')
        kwargs['carusel'] = Burger.objects.filter(show_in_swiper = True)
        kwargs['food'] = cats_with_food
        return kwargs


    

class MainListView(ListView):
    template_name = 'main/list.html'
    paginate_by = 2

    def get_queryset(self):
        cid = self.kwargs.get('id', None)
        query = Burger.objects.order_by('-id')
        if cid:
            cat = Category.objects.filter(path__contains = f"-{cid}-").only('id')
            query = query.filter(category_id__in=cat)
        return query


    def dispatch(self, request, *args, **kwargs):
            cid = kwargs.get('id', None)
            if cid is not None:
                cat = Category.objects.get(id=cid)
                if kwargs.get('slug') != cat.slug:
                    return redirect("main:link",cat.slug, cat.id, permanent=True)
                
            return super().dispatch(request, *args, **kwargs) 
    

    def get_context_data(self, **kwargs):
        cid = self.kwargs.get('id', None)
        if cid is not None:
            cat = Category.objects.get(id=cid)
        context = super().get_context_data(**kwargs)
        context['cat_name'] = cat
        return context

    