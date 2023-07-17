from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class MainIndex(TemplateView):
    template_name = 'main/index.html'
    

class MainListView(ListView):
    pass