from os import name
from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name="index"),
    path('<str:slug>-<int:id>/', MainListView.as_view(), name='link'),
    path('all/', MainListView.as_view(), name='list')
]