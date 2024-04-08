from django.contrib import admin
from .models import Sales, Cart, CartProduct, Order, Product, Category, ProductImagesURL


admin.site.register([Sales, Cart, CartProduct, Order, Product, Category, ProductImagesURL])
# Register your models here.

