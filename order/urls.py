from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path("cart-inc/<int:id>/", cart_inc, name="inc"),
    path("cart-dec/<int:id>/", cart_dec, name="dec"),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]