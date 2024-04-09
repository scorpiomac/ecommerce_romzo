from django.core.management.base import BaseCommand
from apps.cart.models import Product
from apps.cart.utils.stock_forecast import prepare_stock_data, forecast_sales

class Command(BaseCommand):
    help = 'Mise à jour des prévisions de stock pour chaque produit'

    def handle(self, *args, **kwargs):
        self.stdout.write("Préparation des données de vente...")
        df_grouped = prepare_stock_data()
        
        self.stdout.write("Calcul des prévisions de vente...")
        forecasts = forecast_sales(df_grouped)
        print(forecasts.items())
        
        self.stdout.write("Mise à jour des prévisions de stock des produits...")
        for product_id, forecast in forecasts.items():
            product = Product.objects.get(id=product_id)
            product.stock_forecast = int(forecast)
            product.save()
        
        self.stdout.write(self.style.SUCCESS('Les prévisions de stock ont été mises à jour avec succès.'))
