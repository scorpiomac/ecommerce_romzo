# import os
# import django
# from faker import Faker
# import requests
# import random

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")
# django.setup()

# from apps.cart.models import Product, Category, ProductImagesURL  # Ajustez les chemins selon votre projet

# fake = Faker('fr_FR')

# def fetch_unsplash_image(query, color):
#     fas='fashion'
#     access_key = 'lgTvdp0KOa0bQDY3ay87q3zqqyuqINTNQlKPbV6Utqc'
#     page_number = random.randint(1, 10)
#     url = f'https://api.unsplash.com/search/photos?page={page_number}&query={fas}+{query}+{color}&client_id={access_key}'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         results = response.json()['results']
#         if results:
#             selected_image = random.choice(results)
#             return selected_image['urls']['regular']
#     except requests.RequestException as e:
#         print(f"Erreur lors de la requête à l'API Unsplash: {e}")
#     return None

# categories_list = ["Robe", "Chaussures", "Bas", "Hauts", "Pour Enfant", "Pour Femme", "Pour Homme"]
# brands_list = ["Nike", "Adidas", "Levi's", "Puma", "Under Armour", "Gucci", "Prada", "Louis Vuitton"]
# colors_in_english = [("Rouge", "Red"), ("Vert", "Green"), ("Bleu", "Blue"), ("Jaune", "Yellow"), ("Noir", "Black"), ("Blanc", "White"), ("Gris", "Grey"), ("Orange", "Orange"), ("Violet", "Purple"), ("Rose", "Pink"), ("Marron", "Brown"), ("Cyan", "Cyan")]

# def verify_or_create_categories(categories):
#     for cat_name in categories:
#         Category.objects.get_or_create(name=cat_name)

# def add_products(n):
#     for category_name in categories_list:
#         category = Category.objects.get(name=category_name)
#         for _ in range(n):
#             french_color, english_color = random.choice(colors_in_english)
#             gender_cat = random.choice(["Homme", "Femme", "Unisexe"])
#             sub_cat = random.choice(["Vêtement", "Accessoire", "Chaussure"])
#             article_type = random.choice(["Casual", "Sport", "Formel", "Mode"])
#             title = f"{random.choice(['T-shirt', 'Pantalon', 'Chaussure'])} {gender_cat} {article_type} en {french_color}"
#             description = fake.text(max_nb_chars=200)
#             market_price = fake.random_number(digits=5)
#             discount_price = random.randint(0, market_price)
#             brand = random.choice(brands_list)
#             size = fake.random_element(elements=['XS', 'S', 'M', 'L', 'XL'])
#             material = fake.word().capitalize()
#             completelook = fake.text(max_nb_chars=100)
            
#             product = Product(
#                 title=title, 
#                 gender_cat=gender_cat,
#                 sub_cat=sub_cat,
#                 article_type=article_type,
#                 market_price=market_price, 
#                 discount_price=discount_price,
#                 description=description,
#                 brand=brand,
#                 color=french_color,
#                 size=size,
#                 material=material,
#                 completelook=completelook
#             )
#             product.save()
#             product.categories.add(category)
            
#             image_url = fetch_unsplash_image(f"{article_type.lower()}", english_color.lower())
#             if image_url:
#                 ProductImagesURL.objects.create(product=product, image_url=image_url)
#                 print(f'Produit ajouté : {title} avec l\'image {image_url}')
#             else:
#                 print(f'Produit ajouté : {title} sans image')


# print('Début du script de peuplement...')
# verify_or_create_categories(categories_list)
# add_products(5)  # Nombre de produits à ajouter par catégorie
# print('Script de peuplement terminé.')



import os
import django
import requests
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")
django.setup()

from apps.cart.models import Product, Category, ProductImagesURL  # Ajustez le chemin selon votre projet

fake = Faker('fr_FR')

def fetch_unsplash_image(query, color):
    access_key = '1Nb7RbAkqRuBSbk6tuVcbL1RU2ivZ5DeU8fiQ5CR6FU'  # Utilisez votre clé d'accès Unsplash
    page_number = random.randint(1, 10)  # Sélectionnez une page aléatoire pour varier les résultats
    url = f'https://api.unsplash.com/search/photos?page={page_number}&query={query}+{color}&client_id={access_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        results = response.json()['results']
        if results:
            selected_image = random.choice(results)  # Sélection aléatoire d'une image parmi les résultats
            return selected_image['urls']['regular']
    except requests.RequestException as e:
        print(f"Erreur lors de la requête à l'API Unsplash: {e}")
    return None

brands_list = ["Nike", "Adidas", "Levi's", "Puma", "Under Armour", "Gucci", "Prada", "Louis Vuitton"]
categories_list = ["Robe", "Chaussures", "Bas", "Hauts", "Pour Enfant", "Pour Femme", "Pour Homme"]
colors_in_english = [("Rouge", "Red"), ("Vert", "Green"), ("Bleu", "Blue"), ("Jaune", "Yellow"), ("Noir", "Black"), ("Blanc", "White"), ("Gris", "Grey"), ("Orange", "Orange"), ("Violet", "Purple"), ("Rose", "Pink"), ("Marron", "Brown"), ("Cyan", "Cyan")]

def verify_or_create_categories(categories):
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)

def add_products(n):
    for category_name in categories_list:
        category = Category.objects.get(name=category_name)
        for _ in range(n):
            french_color, english_color = random.choice(colors_in_english)
            title = f"{category_name} - {fake.word().capitalize()} {fake.color_name()}"
            description = fake.text(max_nb_chars=200)
            market_price = fake.random_number(digits=3)
            discount_price = random.randint(0, market_price)
            brand = random.choice(brands_list)
            material = fake.word().capitalize()
            completelook = fake.text(max_nb_chars=100)
            gender_cat = random.choice(["Homme", "Femme", "Unisexe"])
            sub_cat = random.choice(["Vêtement", "Accessoire", "Chaussure"])
            article_type = random.choice(["Casual", "Sport", "Formel", "Mode"])
            size = fake.random_element(elements=['XS', 'S', 'M', 'L', 'XL'])
            
            if category_name == "Chaussures":
                query = 'shoes'
            elif category_name == "Robe":
                query = 'dress'
            elif category_name in ["Bas", "Hauts"]:
                query = 'clothing'
            elif category_name == "Pour Enfant":
                query = 'children clothing'
            elif category_name in ["Pour Femme", "Pour Homme"]:
                query = 'fashion'
            else:
                query = 'fashion'
            
            image_url = fetch_unsplash_image(query,english_color.lower())
            
            product = Product(
                            title=title, 
                            gender_cat=gender_cat,
                            sub_cat=sub_cat,
                            article_type=article_type,
                            market_price=market_price, 
                            discount_price=discount_price,
                            description=description,
                            brand=brand,
                            color=french_color,
                            size=size,
                            material=material,
                            completelook=completelook
                        )            
            product.save()
            product.categories.add(category)
            if image_url:
                ProductImagesURL.objects.create(product=product, image_url=image_url)
            print(f'Produit ajouté : {title} avec l\'image {image_url}')


print('Début du script de peuplement...')
verify_or_create_categories(categories_list)
add_products(5)  # Ajoute 5 produits par catégorie
print('Script de peuplement terminé.')
