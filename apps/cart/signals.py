from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    # Définition des catégories principales et de leurs sous-catégories
    categories_structure = [
        "Pour Homme",
        "Pour Femme",
        "Pour Enfant",
        "Hauts",
        "Bas",
        "Chaussures",
        "Robe",
        ]
    

    for category in categories_structure:
        # Création de la catégorie principale
        parent_category, created = Category.objects.get_or_create(name=category)


    
    print("Catégories et sous-catégories prédéfinies créées avec succès.")
