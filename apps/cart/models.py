from django.db import models
from django.db.models.deletion import CASCADE
from apps.accounts.models import *
from django.contrib.auth.models import User
#from apps.seller_accounts.models import *
from django.core.files import File
import os
import urllib.request



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    article_type = models.CharField(max_length=50,null=True)
    market_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    brand = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=200,null=True)
    size = models.CharField(max_length=5,default="S")
    material = models.CharField(max_length=200,null=True)
    completelook = models.TextField(null=True)
    
    def __str__(self):
        return self.title

class ProductImagesFiles(models.Model):
    product = models.ForeignKey(Product,on_delete=CASCADE)
    image_file = models.ImageField(upload_to="products",blank=True)

class ProductImagesURL(models.Model):
    product = models.ForeignKey(Product,on_delete=CASCADE)
    image_url = models.URLField(max_length=500,blank=True)

    def __str__(self):
        return self.product.title
    
class ProductRecommendation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='recommendation')
    recommended_products = models.ManyToManyField(Product, related_name='recommended_by', blank=True)

    def __str__(self):
        return f"Recommandations pour {self.product.name}"

    

from django.db import models

class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.profile.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} de {self.product.title} dans le panier"

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande #{self.id} par {self.profile.user.username}"
    
    def get_total(self):
        total = sum(item.get_total() for item in self.items.all())
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
    
    def get_total(self):
        return self.quantity * (self.product.market_price - self.product.discount_price)