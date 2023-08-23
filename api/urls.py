from django.urls import path
from .views import ApiCategory

app_name = 'api'

urlpatterns = [
    path('category/', ApiCategory.as_view(), name='category')
]