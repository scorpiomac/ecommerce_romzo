from django.contrib import admin
from .models import Sales, Cart, CartProduct, Order, Product, Category


admin.site.register([Sales, Cart, CartProduct, Order, Product, Category])
# Register your models here.

