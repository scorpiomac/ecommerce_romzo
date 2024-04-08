from django.contrib import admin
<<<<<<< HEAD
from .models import Sales, Cart, CartProduct, Order, Product, Category, ProductImagesURL


admin.site.register([Sales, Cart, CartProduct, Order, Product, Category, ProductImagesURL])
# Register your models here.
=======
# from .models import Sales, Cart, CartProduct, Order, Product, Category,ProductImagesURL
from .models import Order


# admin.site.register([Sales, Cart, CartProduct, Order, Product,ProductImagesURL, Category])
# # Register your models here.

admin.site.register([Order])

>>>>>>> db98fac77d4d437644e88adf7c55cfb43ba5305a

