from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

from main.models import Burger

class Order(models.Model):
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2

    PAYMENT_STATUS_NONE = 0
    PAYMENT_STATUS_PREPARE = 1
    PAYMENT_STATUS_PAID = 2
    PAYMENT_STATUS_CANCELLED = 3


    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    addres = models.TextField()
    zip = models.CharField(max_length=10)
    total_price = models.IntegerField()
    status = models.IntegerField(choices=(
        (STATUS_NEW,"YANGI"),
        (STATUS_ACCEPTED,'QABUL QILINGAN'),
        (STATUS_REJECTED,'INKOR QILINGAN')
    ), verbose_name='Status')
    payment_status = models.SmallIntegerField(choices=(
        (PAYMENT_STATUS_NONE, 'NOANIQ'),
        (PAYMENT_STATUS_PREPARE, 'JARAYONDA'),
        (PAYMENT_STATUS_PAID, 'TOLANGAN'),
        (PAYMENT_STATUS_CANCELLED, 'BEKOR QILINGAN')
    ))
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    burger = models.ForeignKey(Burger, on_delete=models.RESTRICT)
    price = models.IntegerField()
    amount = models.IntegerField()
