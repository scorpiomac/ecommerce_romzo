# import random
# from django.db.models import Q
# from apps.cart.models import Product, Category  # Remplacez 'votre_application' par le nom de votre application

# import os
# import django
# import requests
# import random
# from faker import Faker

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")
# django.setup()

# # Modèles de titres pour chaque catégorie avec des placeholders
# modeles_titres = {
#     'Robe': ['Robe de soirée {couleur}', 'Robe d\'été {couleur}', 'Robe de cocktail {couleur}', 'Robe longue {couleur}', 'Robe à fleurs {couleur}'],
#     'Chaussures': ['Chaussures de sport {couleur}', 'Chaussures de ville {couleur}', 'Bottes {couleur}', 'Escarpins {couleur}'],
#     'Bas': ['Jeans {couleur}', 'Leggings {couleur}', 'Short {couleur}', 'Pantalon {couleur}'],
#     'Hauts': ['T-shirt {couleur}', 'Chemise {couleur}', 'Pull {couleur}', 'Blouse {couleur}', 'Sweatshirt {couleur}'],
#     'Pour Enfant': ['Ensemble pour enfant {couleur}', 'Jouet {couleur}', 'Pyjama {couleur}', 'Chapeau pour enfant {couleur}'],
#     'Pour Femme': ['Accessoire pour femme {couleur}', 'Sac à main {couleur}', 'Écharpe {couleur}', 'Collier {couleur}'],
#     'Pour Homme': ['Montre {couleur}', 'Portefeuille {couleur}', 'Cravate {couleur}', 'Ceinture {couleur}'],
# }


# # Descriptions générales pour chaque catégorie
# descriptions = {
#     'Robe': [
#         "Une sélection exclusive de robes {couleur} pour toutes occasions. Confort et élégance garantis. Trouvez la robe parfaite pour mettre en valeur votre style unique.",
#         "Sublimez votre silhouette avec nos robes {couleur} tendance. De la robe de soirée à la robe d'été, trouvez votre bonheur parmi notre collection variée.",
#         "Découvrez nos robes {couleur} conçues pour vous faire rayonner. Que ce soit pour une soirée spéciale ou une journée décontractée, adoptez le style qui vous ressemble.",
#         "Optez pour le raffinement avec nos robes {couleur} élégantes. Des coupes et des tissus de qualité pour un look qui fera sensation à chaque occasion.",
#         "Trouvez la robe parfaite parmi notre sélection variée de robes {couleur}. Du style classique au moderne, nous avons ce qu'il vous faut pour être au top de la mode."
#     ],
#     'Chaussures': [
#         "Découvrez notre gamme de chaussures {couleur} pour un confort optimal et un style inégalé. Des chaussures conçues pour accompagner vos pas avec élégance et assurance.",
#         "Parcourez notre sélection de chaussures {couleur} pour hommes et femmes. Que vous recherchiez des baskets pour le sport ou des chaussures habillées, nous avons ce qu'il vous faut.",
#         "Optez pour le confort et l'élégance avec nos chaussures {couleur} de haute qualité. Parfaites pour compléter votre tenue avec style et assurance.",
#         "Des chaussures {couleur} qui allient style et praticité. Que ce soit pour une journée de travail ou une sortie entre amis, soyez toujours à l'aise et tendance.",
#         "Explorez notre collection de chaussures {couleur} et trouvez la paire parfaite pour chaque occasion. Confortables, durables et toujours à la mode."
#     ],
#     'Bas': [
#         "Notre collection de bas {couleur} combine style et confort. Parfait pour votre garde-robe quotidienne. Optez pour des bas qui vous suivront partout avec style.",
#         "Affirmez votre style avec nos bas {couleur} à la fois tendance et confortables. Des jeans aux leggings, trouvez le bas parfait pour compléter votre look.",
#         "Que vous préfériez un style décontracté ou sophistiqué, nos bas {couleur} sauront répondre à toutes vos envies. Découvrez notre sélection dès maintenant.",
#         "Des bas {couleur} conçus pour s'adapter à votre mode de vie actif. Résistants et confortables, ils vous accompagneront dans toutes vos aventures.",
#         "Optez pour des bas {couleur} de qualité supérieure. Confortables, durables et élégants, ils deviendront rapidement des indispensables de votre garde-robe."
#     ],
#     'Hauts': [
#         "Explorez nos hauts {couleur} pour un look casual ou formel. Qualité et durabilité assurées. Des hauts qui s'adaptent à votre style de vie, que ce soit au travail ou en soirée.",
#         "Exprimez votre style avec nos hauts {couleur} tendance. T-shirts, chemises, pulls, trouvez votre bonheur parmi notre sélection variée.",
#         "Découvrez nos hauts {couleur} conçus pour allier confort et élégance. Parfaits pour toutes les occasions, ils deviendront vite indispensables dans votre garde-robe.",
#         "Affirmez votre personnalité avec nos hauts {couleur} originaux. Des motifs uniques et des coupes modernes pour un look qui ne passe pas inaperçu.",
#         "Optez pour des hauts {couleur} de qualité supérieure. Confortables, résistants et stylés, ils sont parfaits pour compléter votre tenue avec classe."
#     ],
#     'Pour Enfant': [
#         "Tout pour les enfants: des vêtements {couleur} aux jouets amusants et éducatifs. Offrez à vos enfants des produits de qualité qui stimuleront leur imagination et leur créativité.",
#         "Découvrez notre sélection de vêtements {couleur} pour enfants, à la fois confortables et stylés. De quoi les faire rayonner au quotidien.",
#         "Parcourez notre collection de jouets {couleur} pour enfants et offrez-leur des heures de divertissement et d'apprentissage. Des jouets sûrs et ludiques pour tous les âges.",
#         "Des vêtements {couleur} pour enfants qui allient confort et style. Des coupes adaptées à leurs besoins et des couleurs vives pour égayer leur quotidien.",
#         "Offrez à vos enfants des vêtements {couleur} de qualité supérieure. Confortables, durables et tendance, ils les accompagneront dans toutes leurs aventures."
#     ],
#     'Pour Femme': [
#         "Accessoires {couleur} essentiels pour femme. Ajoutez une touche d'élégance à votre tenue. Des accessoires qui complètent votre style avec raffinement et distinction.",
#         "Sublimez votre look avec nos accessoires {couleur} tendance. Sacs à main, écharpes, bijoux, découvrez notre sélection pour une allure irrésistible.",
#         "Que vous soyez à la recherche d'un accessoire pratique ou d'un bijou élégant, notre collection d'accessoires {couleur} saura répondre à toutes vos envies.",
#         "Des accessoires {couleur} qui ajoutent une touche de sophistication à votre tenue. Des pièces intemporelles qui complèteront parfaitement votre style.",
#         "Optez pour des accessoires {couleur} de qualité supérieure. Conçus pour durer et pour sublimer toutes vos tenues, ils vous accompagneront en toutes occasions."
#     ],
#     'Pour Homme': [
#         "Sélection de produits {couleur} pour homme. Conçu pour le style de vie moderne. Des produits qui reflètent votre personnalité et votre dynamisme, où que vous alliez.",
#         "Affirmez votre style avec nos produits {couleur} pour homme. Montres, portefeuilles, ceintures, trouvez les accessoires parfaits pour compléter votre look.",
#         "Découvrez notre gamme de produits {couleur} pour homme, alliant qualité et élégance. Des essentiels pour un dressing masculin aussi pratique que stylé.",
#         "Des produits {couleur} pour homme qui allient confort et style. Des matériaux de qualité et des coupes impeccables pour une allure toujours au top.",
#         "Optez pour des produits {couleur} de qualité supérieure. Durables, résistants et élégants, ils seront vos compagnons de confiance au quotidien."
#     ]
# }


# import random

# def generer_titre_et_description(produit, categorie):
#     # Choisir un modèle de titre au hasard pour la catégorie du produit
#     modele_titre = random.choice(modeles_titres[categorie])
#     titre = modele_titre.format(couleur=produit.color)
    
#     # Choisir une description au hasard pour la catégorie du produit
#     description = random.choice(descriptions[categorie]).format(couleur=produit.color)
    
#     return titre, description


# def mettre_a_jour_produits():
#     for categorie_nom in modeles_titres.keys():
#         categorie = Category.objects.get(name=categorie_nom)
#         produits = Product.objects.filter(categories=categorie)
        
#         for produit in produits:
#             titre, description = generer_titre_et_description(produit, categorie)
#             produit.title = titre
#             produit.description = description
#             produit.save()

# # Appeler la fonction pour mettre à jour les produits
# mettre_a_jour_produits()



import random
import os
import django

# Assurez-vous que le chemin d'accès et le nom de votre projet Django sont corrects
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")
django.setup()

from apps.cart.models import Product, Category  # Ajustez ce chemin selon l'organisation de votre projet

from faker import Faker
fake = Faker()

# Modèles de titres et descriptions ici (non modifiés, pour éviter la redondance)
modeles_titres = {
    'Robe': ['Robe de soirée {couleur}', 'Robe d\'été {couleur}', 'Robe de cocktail {couleur}', 'Robe longue {couleur}', 'Robe à fleurs {couleur}'],
    'Chaussures': ['Chaussures de sport {couleur}', 'Chaussures de ville {couleur}', 'Bottes {couleur}', 'Escarpins {couleur}'],
    'Bas': ['Jeans {couleur}', 'Leggings {couleur}', 'Short {couleur}', 'Pantalon {couleur}'],
    'Hauts': ['T-shirt {couleur}', 'Chemise {couleur}', 'Pull {couleur}', 'Blouse {couleur}', 'Sweatshirt {couleur}'],
    'Pour Enfant': ['Ensemble pour enfant {couleur}', 'Jouet {couleur}', 'Pyjama {couleur}', 'Chapeau pour enfant {couleur}'],
    'Pour Femme': ['Accessoire pour femme {couleur}', 'Sac à main {couleur}', 'Écharpe {couleur}', 'Collier {couleur}'],
    'Pour Homme': ['Montre {couleur}', 'Portefeuille {couleur}', 'Cravate {couleur}', 'Ceinture {couleur}'],
}


# Descriptions générales pour chaque catégorie
descriptions = {
    'Robe': [
        "Une sélection exclusive de robes {couleur} pour toutes occasions. Confort et élégance garantis. Trouvez la robe parfaite pour mettre en valeur votre style unique.",
        "Sublimez votre silhouette avec nos robes {couleur} tendance. De la robe de soirée à la robe d'été, trouvez votre bonheur parmi notre collection variée.",
        "Découvrez nos robes {couleur} conçues pour vous faire rayonner. Que ce soit pour une soirée spéciale ou une journée décontractée, adoptez le style qui vous ressemble.",
        "Optez pour le raffinement avec nos robes {couleur} élégantes. Des coupes et des tissus de qualité pour un look qui fera sensation à chaque occasion.",
        "Trouvez la robe parfaite parmi notre sélection variée de robes {couleur}. Du style classique au moderne, nous avons ce qu'il vous faut pour être au top de la mode."
    ],
    'Chaussures': [
        "Découvrez notre gamme de chaussures {couleur} pour un confort optimal et un style inégalé. Des chaussures conçues pour accompagner vos pas avec élégance et assurance.",
        "Parcourez notre sélection de chaussures {couleur} pour hommes et femmes. Que vous recherchiez des baskets pour le sport ou des chaussures habillées, nous avons ce qu'il vous faut.",
        "Optez pour le confort et l'élégance avec nos chaussures {couleur} de haute qualité. Parfaites pour compléter votre tenue avec style et assurance.",
        "Des chaussures {couleur} qui allient style et praticité. Que ce soit pour une journée de travail ou une sortie entre amis, soyez toujours à l'aise et tendance.",
        "Explorez notre collection de chaussures {couleur} et trouvez la paire parfaite pour chaque occasion. Confortables, durables et toujours à la mode."
    ],
    'Bas': [
        "Notre collection de bas {couleur} combine style et confort. Parfait pour votre garde-robe quotidienne. Optez pour des bas qui vous suivront partout avec style.",
        "Affirmez votre style avec nos bas {couleur} à la fois tendance et confortables. Des jeans aux leggings, trouvez le bas parfait pour compléter votre look.",
        "Que vous préfériez un style décontracté ou sophistiqué, nos bas {couleur} sauront répondre à toutes vos envies. Découvrez notre sélection dès maintenant.",
        "Des bas {couleur} conçus pour s'adapter à votre mode de vie actif. Résistants et confortables, ils vous accompagneront dans toutes vos aventures.",
        "Optez pour des bas {couleur} de qualité supérieure. Confortables, durables et élégants, ils deviendront rapidement des indispensables de votre garde-robe."
    ],
    'Hauts': [
        "Explorez nos hauts {couleur} pour un look casual ou formel. Qualité et durabilité assurées. Des hauts qui s'adaptent à votre style de vie, que ce soit au travail ou en soirée.",
        "Exprimez votre style avec nos hauts {couleur} tendance. T-shirts, chemises, pulls, trouvez votre bonheur parmi notre sélection variée.",
        "Découvrez nos hauts {couleur} conçus pour allier confort et élégance. Parfaits pour toutes les occasions, ils deviendront vite indispensables dans votre garde-robe.",
        "Affirmez votre personnalité avec nos hauts {couleur} originaux. Des motifs uniques et des coupes modernes pour un look qui ne passe pas inaperçu.",
        "Optez pour des hauts {couleur} de qualité supérieure. Confortables, résistants et stylés, ils sont parfaits pour compléter votre tenue avec classe."
    ],
    'Pour Enfant': [
        "Tout pour les enfants: des vêtements {couleur} aux jouets amusants et éducatifs. Offrez à vos enfants des produits de qualité qui stimuleront leur imagination et leur créativité.",
        "Découvrez notre sélection de vêtements {couleur} pour enfants, à la fois confortables et stylés. De quoi les faire rayonner au quotidien.",
        "Parcourez notre collection de jouets {couleur} pour enfants et offrez-leur des heures de divertissement et d'apprentissage. Des jouets sûrs et ludiques pour tous les âges.",
        "Des vêtements {couleur} pour enfants qui allient confort et style. Des coupes adaptées à leurs besoins et des couleurs vives pour égayer leur quotidien.",
        "Offrez à vos enfants des vêtements {couleur} de qualité supérieure. Confortables, durables et tendance, ils les accompagneront dans toutes leurs aventures."
    ],
    'Pour Femme': [
        "Accessoires {couleur} essentiels pour femme. Ajoutez une touche d'élégance à votre tenue. Des accessoires qui complètent votre style avec raffinement et distinction.",
        "Sublimez votre look avec nos accessoires {couleur} tendance. Sacs à main, écharpes, bijoux, découvrez notre sélection pour une allure irrésistible.",
        "Que vous soyez à la recherche d'un accessoire pratique ou d'un bijou élégant, notre collection d'accessoires {couleur} saura répondre à toutes vos envies.",
        "Des accessoires {couleur} qui ajoutent une touche de sophistication à votre tenue. Des pièces intemporelles qui complèteront parfaitement votre style.",
        "Optez pour des accessoires {couleur} de qualité supérieure. Conçus pour durer et pour sublimer toutes vos tenues, ils vous accompagneront en toutes occasions."
    ],
    'Pour Homme': [
        "Sélection de produits {couleur} pour homme. Conçu pour le style de vie moderne. Des produits qui reflètent votre personnalité et votre dynamisme, où que vous alliez.",
        "Affirmez votre style avec nos produits {couleur} pour homme. Montres, portefeuilles, ceintures, trouvez les accessoires parfaits pour compléter votre look.",
        "Découvrez notre gamme de produits {couleur} pour homme, alliant qualité et élégance. Des essentiels pour un dressing masculin aussi pratique que stylé.",
        "Des produits {couleur} pour homme qui allient confort et style. Des matériaux de qualité et des coupes impeccables pour une allure toujours au top.",
        "Optez pour des produits {couleur} de qualité supérieure. Durables, résistants et élégants, ils seront vos compagnons de confiance au quotidien."
    ]
}
def generer_titre_et_description(produit, categorie_nom):
    categorie = Category.objects.get(name=categorie_nom)
    # Choisir un modèle de titre au hasard pour la catégorie du produit
    modele_titre = random.choice(modeles_titres[categorie_nom])
    titre = modele_titre.format(couleur=produit.color)
    
    # Choisir une description au hasard pour la catégorie du produit
    description = random.choice(descriptions[categorie_nom]).format(couleur=produit.color, matiere=fake.word(), style=fake.word(), occasion=fake.sentence())
    
    return titre, description

def mettre_a_jour_produits():
    for categorie_nom in modeles_titres.keys():
        categorie = Category.objects.get(name=categorie_nom)
        produits = Product.objects.filter(categories=categorie)
        
        for produit in produits:
            titre, description = generer_titre_et_description(produit, categorie_nom)
            produit.title = titre
            produit.description = description
            produit.save()

# Appeler la fonction pour mettre à jour les produits
mettre_a_jour_produits()
