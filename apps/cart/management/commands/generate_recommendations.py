from django.core.management.base import BaseCommand
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from apps.cart.models import Product, ProductRecommendation
import nltk


# Téléchargez la liste des mots vides en français de NLTK
nltk.download('stopwords')
from nltk.corpus import stopwords
french_stop_words = stopwords.words('french')


class Command(BaseCommand):
    help = 'Génère des recommandations de produits basées sur le contenu'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        
        for p in products:
            p.cat=[]
            print(p.categories.all())
            if p.categories.all() is not None:
                for i in p.categories.all():
                    p.cat.append(i.name)
        


        features_text = [' '.join(filter(None, [p.title, ", ".join(p.cat), 
                                                p.article_type, p.brand]))
                         for p in products]
        product_ids = [p.id for p in products]

        tfidf = TfidfVectorizer(stop_words=french_stop_words)
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
