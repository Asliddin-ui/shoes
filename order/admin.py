from django.contrib import admin

from .models import Order, OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'address', 'zip', 'total_price']


@admin.register(OrderProduct)
class OrderBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'burger', 'price', 'amount']