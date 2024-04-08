
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "apps.cart"
urlpatterns = [

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('update-cart-item/', views.update_cart_item, name='update-cart-item'),
    path('remove-from-cart/', views.remove_from_cart, name='remove-from-cart'),

    
    
    path('my-cart/',views.mycart, name="mycart"),
    
    path("empty-cart/", views.emptycart, name="empty-cart"),
    path('checkout/', views.checkout_summary, name='checkout'),
    path('checkout/', views.checkout, name='payer'),
    path('thank-you/<int:order_number>/<str:email>/', views.thank_you, name='thanks'),


    # path("checkoutdetails/", views.checkoutdetails, name="checkoutdetails")

]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)