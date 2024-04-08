from django.contrib import admin
from .models import  Cart, CartItem, Order, Product, Category,ProductImagesURL,OrderItem
from .models import Order


# admin.site.register([Sales, Cart, CartProduct, Order, Product,ProductImagesURL, Category])
# # Register your models here.

admin.site.register([Cart, CartItem, Order, Product, Category,ProductImagesURL,OrderItem])


