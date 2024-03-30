from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    # Définition des catégories principales et de leurs sous-catégories
    categories_structure = {
        "Pour Homme": ["Hauts", "Bas", "Chaussures"],
        "Pour Femme": ["Hauts", "Bas", "Chaussures", "Robes"],
        "Pour Enfant": ["Hauts", "Bas", "Chaussures"]
    }

    for parent_name, sub_categories in categories_structure.items():
        # Création de la catégorie principale
        parent_category, created = Category.objects.get_or_create(name=parent_name)

        # Création des sous-catégories
        for sub_cat_name in sub_categories:
            Category.objects.get_or_create(name=sub_cat_name, parent=parent_category)
    
    
