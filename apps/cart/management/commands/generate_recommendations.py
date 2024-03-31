from django.core.management.base import BaseCommand
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from apps.cart.models import Product, ProductRecommendation

class Command(BaseCommand):
    help = 'Génère des recommandations de produits basées sur le contenu'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        features_text = [' '.join(filter(None, [p.description, p.gender_cat, p.sub_cat,
                                                p.articel_type, p.brand, p.color, p.material]))
                         for p in products]
        product_ids = [p.id for p in products]

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(features_text)

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        for idx, product_id in enumerate(product_ids):
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            similar_product_ids = [product_ids[i[0]] for i in sim_scores[1:6]]  # Top 5
            
            recommended_products = Product.objects.filter(id__in=similar_product_ids)
            
            recommendation, _ = ProductRecommendation.objects.get_or_create(product_id=product_id)
            recommendation.recommended_products.set(recommended_products)
            recommendation.save()

        self.stdout.write(self.style.SUCCESS('Recommandations basées sur le contenu générées avec succès.'))
