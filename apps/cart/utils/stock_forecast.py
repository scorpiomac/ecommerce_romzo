import pandas as pd
from django.db.models import Sum
from apps.cart.models import Product, OrderItem, Order
import statsmodels.api as sm
import numpy as np

def prepare_stock_data():
    # Récupérer toutes les commandes payées
    orders = Order.objects.filter(is_paid=False).prefetch_related('items')
    
    data = []
    for order in orders:
        for item in order.items.all():
            data.append({
                'date': order.created_at.date(),
                'product_id': item.product.id,
                'quantity_sold': item.quantity
            })
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df_grouped = df.groupby(['product_id', pd.Grouper(key='date', freq='M')]).agg({'quantity_sold': 'sum'}).reset_index()

    return df_grouped

def forecast_sales(df_grouped):
    forecasts = {}
    
    for product_id, group in df_grouped.groupby('product_id'):
        ts = group.set_index('date')['quantity_sold']
        ts = ts.asfreq('M', fill_value=0)

        # Assurer que ts est un array numpy de floats pour éviter des problèmes de type
        ts_array = np.array(ts, dtype=float)
        
        # Ajuster un modèle ARIMA
        model = sm.tsa.ARIMA(ts_array, order=(1, 1, 1))
        result = model.fit()
        
        # Prévoir la demande pour les prochains mois
        forecast = result.forecast(steps=3)  # Prévoir les 3 prochains mois
        forecasts[product_id] = forecast[0]

    return forecasts
