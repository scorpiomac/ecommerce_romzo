from django.contrib import admin

from .models import  Cart, CartItem, Order, Product, Category,ProductImagesURL,OrderItem

admin.site.register([Cart, CartItem, Order, Product, Category,ProductImagesURL,OrderItem])


