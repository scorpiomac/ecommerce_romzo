import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from apps.cart.models import Product, ProductRecommendation

def create_feature_text(product):
    # Combinez les attributs textuels pertinents en une seule chaîne de texte
    attributes = [product.description, product.gender_cat, product.sub_cat,
                  product.articel_type, product.brand, product.color, product.material]
    return ' '.join(filter(None, attributes))  # Filtrer les valeurs None

def generate_content_based_recommendations():
    products = Product.objects.all()
    features_text = [create_feature_text(p) for p in products]
    product_ids = [p.id for p in products]

    # Vectorisation TF-IDF des textes des caractéristiques
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(features_text)

    # Calcul de la similarité cosinus
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    for idx, product_id in enumerate(product_ids):
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        similar_product_ids = [product_ids[i[0]] for i in sim_scores[1:6]]  # Top 5
        
        recommended_products = Product.objects.filter(id__in=similar_product_ids)
        
        recommendation, _ = ProductRecommendation.objects.get_or_create(product_id=product_id)
        recommendation.recommended_products.set(recommended_products)
        recommendation.save()

    print("Recommandations basées sur le contenu générées avec succès.")
