from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Page
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView, ListView
from main.models import Category, Burger, PageModel, WhyModel


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
            # cat = Category.objects.filter(path__contains = f"-{cid}-").only('id')
            query = query.select_related('category').filter(category__path__contains = f"-{cid}-")
        return query


    def dispatch(self, request, *args, **kwargs):
        cid = kwargs.get('id', None)
        if cid is not None:
            cat = Category.objects.get(id=cid)
            if kwargs.get('slug') != cat.slug:
                return redirect("main:link",cat.slug, cat.id, permanent=True)
            
        return super().dispatch(request, *args, **kwargs) 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bur = context['object_list']
        if bur:
            fb = bur[0]
            context['cat_name'] = fb.category.name
        
        return context

class AboutUsView(DetailView):
    model = PageModel
    template_name = 'main/contacts.html' 

    # def get_object(self, queryset=None):
    #     slug = self.kwargs.get('slug', None)
    #     if slug:
    #         try:
    #             return PageModel.objects.select_related('category').get(category__slug=slug)
    #         except PageModel.DoesNotExist:
    #             pass
    #     return None

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get('pk')
        try:
            page = PageModel.objects.select_related('category').get(category__id=slug)
        except (PageModel.DoesNotExist, ObjectDoesNotExist):
            return redirect("main:index")
        
        return super().dispatch(request, *args, **kwargs)

class MainBurgerView(DetailView):
    model = Burger
    template_name = 'main/book.html'
    context_object_name = 'burger'

    def get_object(self, queryset=None ):
        if not self.object:
            self.object = super().get_object(queryset=queryset)
        return super().get_object(queryset)


    def dispatch(self, request,*args, **kwargs):
        self.object = None
        obj = self.get_object()
        if kwargs.get('slug') != obj.slug:
            return redirect('main:burger', obj.slug, obj.id, permanent=True)

        return super().dispatch(request, *args, **kwargs)
       