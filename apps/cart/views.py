from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from sympy import DotProduct
from apps.cart.models import *

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
# productcount=0
#productcount = CartProduct.objects.filter(cart=cart).count()
# @login_required
# def addtocart(request, pid):
#     url_pid = pid
#     product_obj = Product.objects.get(id=url_pid)
#     profile = Profile.objects.get(id=request.user.profile.id)
#     #cart_id = request.session.get("cart_id", None)
#     cart_obj= Cart.objects.filter(profile=profile, ordered='False').last()

#     if cart_obj:
#         cart_id=cart_obj.id
#         cart_obj = Cart.objects.get(id=cart_id)
#         this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)

#         if this_product_in_cart.exists():
#             cartproduct = this_product_in_cart.last()
#             cartproduct.quantity += 1
#             cartproduct.subtotal += product_obj.market_price
#             cartproduct.save()
#             cart_obj.total += product_obj.market_price
#             cart_obj.save()
        
#         else:
#             cartproduct = CartProduct.objects.create(
#                 cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
#             cart_obj.total += product_obj.market_price
#             cart_obj.save()
#             productcount = CartProduct.objects.filter(cart=cart_obj).count()
            
#     else:
#         cart_obj = Cart.objects.create(total=0, profile=profile)
#         #request.session['cart_id'] = cart_obj.id
#         cartproduct = CartProduct.objects.create(
#             cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
#         cart_obj.total += product_obj.market_price
#         cart_obj.save()
        
    
#     #return render(request, "proadded.html")
#     messages.success(request,'Item added to Cart.')
#     return redirect('apps.cart:mycart')

# @login_required
# def mycart(request):
#     profile = Profile.objects.get(id=request.user.profile.id)
#     #cart_id = request.session.get("cart_id", None)
#     cart= Cart.objects.filter(profile=profile, ordered='False').last()
#     if cart:
#         cart = Cart.objects.get(id=cart.id)        
            
#     else:
#         cart = Cart.objects.create(total=0, profile=profile)
#     #productcount = request.session.get('productcount')    
#     cartproducts = cart.cartproduct_set.all().order_by('-id')
#     return render(request, 'shop-cart.html', {'cart': cart,'cartproducts':cartproducts})



@login_required
def mycart(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        try:
            cart = Cart.objects.get(profile=profile)  # Récupérer le panier de l'utilisateur
            cart_items = CartItem.objects.filter(cart=cart)  # Récupérer tous les articles dans le panier
        except Cart.DoesNotExist:
            cart_items = None  # Gérer le cas où le panier n'existe pas

        context = {
            'cart_items': cart_items
        }
        return render(request, 'shop-cart.html', context)  # Rendre le template avec les articles du panier
    else:
        return render(request, 'shop-cart.html', {'cart_items': None})








@require_http_methods(["POST"])
def emptycart(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        try:
            cart = Cart.objects.get(profile=profile)
            CartItem.objects.filter(cart=cart).delete()  # Supprimer tous les articles du panier
            return JsonResponse({'status': 'success', 'message': 'Panier vidé avec succès'})
        except Cart.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Panier non trouvé'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté'})


# @login_required
# def checkoutdetails(request):
#     user = request.user
#     profile = Profile.objects.get(id=request.user.profile.id)
#     address= Address.objects.filter(profile=profile,isprimary=True).last()
#     # address_list= Address.objects.all().order_by('-id')
#     cart = Cart.objects.filter(profile=profile, ordered='False').last()
#     cartproduct = CartProduct.objects.filter(cart=cart)
#     order = Order.objects.filter(cart=cart).last()
    
#     if request.user.is_authenticated:
#         if cart:
#             if request.method == 'POST':
#                 addr = request.POST.get('address')
#                 if addr == 'new':
#                     addline = request.POST.get('addline')
#                     city = request.POST.get('city')
#                     state = request.POST.get('state')
#                     pincode = request.POST.get('zipcode')
#                     firstname = request.POST.get('firstname')
#                     lastname = request.POST.get('lastname')
#                     email = request.POST.get('emailadd')
#                     mob_no = request.POST.get('phoneno')
#                 else:
#                     addline = address.addline
#                     city = address.city
#                     state = address.state
#                     pincode = address.pincode
#                     firstname = user.first_name
#                     lastname = user.last_name
#                     email = user.email
#                     mob_no = profile.mob_no

#                 ordered_by = firstname +" "+ lastname
#                 shipping_address = addline +" "+ city +" "+ state +" - "+ str(pincode)
#                 subtotal = cart.total
#                 total = subtotal
#                 order_status = "Order Processing"
                


#                 order, created = Order.objects.update_or_create(
#                     cart_id=cart.id,
#                     defaults={'ordered_by':ordered_by, 'shipping_address':shipping_address,'mob_no':mob_no,'email':email,'subtotal':subtotal, 'order_status':order_status, 'total':total},
#                 )
#                 # completing order here
#                 cart.ordered = True
#                 cart.save(update_fields=['ordered'])
#                 cart = Cart.objects.create(total=0, profile=profile)
#                 for cp in cartproduct:
#                     sale= Sales.objects.filter(product=cp.product, rate=cp.rate).last()
#                     sale.quantity += cp.quantity
#                     sale.subtotal += cp.subtotal
#                     sale.save(update_fields=['quantity','subtotal'])
                
#                 messages.success(request,'Order Placed.')
#                 return redirect("apps.accounts:orders")

#         else:
#             messages.warning(request,'Add iteems to Cart.')
#             return redirect("apps.main:showallproducts")
         
#     else:
#         messages.warning(request,'You are not signed in.')
#         return redirect("apps.accounts:signin")
#     cartproducts = cart.cartproduct_set.all().order_by('-id')
#     return render(request, "checkout-details.html",{'profile': profile, 'address':address, 'order':order, 'cart': cart,'cartproducts':cartproducts})


@require_http_methods(["POST"])
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        profile = request.user.profile
        cart, created = Cart.objects.get_or_create(profile=profile)
        
        # Gestion de l'ajout ou mise à jour de l'item dans le panier
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity  # Augmenter la quantité existante
        else:
            cart_item.quantity = quantity  # Définir la quantité pour un nouvel item
        cart_item.save()
        
        return JsonResponse({'status': 'success', 'message': 'Produit ajouté au panier'})
    return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté'})


@require_http_methods(["POST"])
def update_cart_item(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        profile = request.user.profile
        try:
            cart_item = CartItem.objects.get(cart__profile=profile, product=product)
            if quantity <= 0:
                cart_item.delete()  # Supprimer l'item si la quantité est zéro ou moins
            else:
                cart_item.quantity = quantity
                cart_item.save()
            return JsonResponse({'status': 'success', 'message': 'Panier mis à jour'})
        except CartItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Article non trouvé dans le panier'})
    return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté'})


@require_http_methods(["POST"])
def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        profile = request.user.profile
        try:
            cart_item = CartItem.objects.get(cart__profile=profile, product=product)
            cart_item.delete()
            return JsonResponse({'status': 'success', 'message': 'Produit retiré du panier'})
        except CartItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Article non trouvé dans le panier'})
    return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté'})




@login_required
def checkout(request):
    if request.method == 'POST':
        profile = request.user.profile
        payment_method = request.POST.get('payment_method')
        
        cart = Cart.objects.get(profile=profile)
        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items:
            return redirect('mycart')  # Assurez-vous que 'mycart' est bien l'alias de l'URL de votre page panier

        # Création de la commande
        order = Order.objects.create(profile=profile)

        # Transfert des articles du panier à la commande
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            item.delete()  # Suppression des articles du panier

        # Redirection vers la page de remerciement avec les informations de commande
        return redirect(reverse('thank_you', kwargs={'order_number': order.id, 'email': profile.user.email}))

       

    return redirect('mycart')
    

from django.shortcuts import render
from .models import Cart, CartItem, Address, Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout_summary(request):

    if request.method == 'POST':
        profile = request.user.profile
        payment_method = request.POST.get('payment_method')
        
        cart = Cart.objects.get(profile=profile)
        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items:
            return redirect('apps.cart:mycart')  # Assurez-vous que 'mycart' est bien l'alias de l'URL de votre page panier

        # Création de la commande
        order = Order.objects.create(profile=profile)

        # Transfert des articles du panier à la commande
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            item.delete()  # Suppression des articles du panier

        # Redirection vers la page de remerciement avec les informations de commande
        return redirect(reverse('apps.cart:thanks', kwargs={'order_number': order.id, 'email': profile.user.email}))


    profile = request.user.profile
    cart, created = Cart.objects.get_or_create(profile=profile)
    cart_items = CartItem.objects.filter(cart=cart)
    addresses = Address.objects.filter(profile=profile)

    if cart_items.exists():
        subtotal = sum(item.product.discount_price * item.quantity if item.product.discount_price else item.product.market_price * item.quantity for item in cart_items)
        # Supposons que la livraison est gratuite pour simplifier, ajustez selon votre logique
        shipping = 0
        total = subtotal + shipping
    else:
        subtotal, shipping, total = 0, 0, 0

    context = {
        'cart_items': cart_items,
        'addresses': addresses,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total
    }
    return render(request, 'checkout-details.html', context)


def thank_you(request, order_number, email):
    return render(request, 'thank_you.html', {'order_number': order_number, 'email': email})
