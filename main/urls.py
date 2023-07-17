from django.urls import path
from .views import *

urlpatterns = [
    path('', MainIndex.as_view(), name="index"),
]