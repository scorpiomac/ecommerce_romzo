import requests

def fetch_unsplash_image(query='product'):
    access_key = '1-uvdXiADyuaPAgkWIDuzF45nrbwC3FLJJpRatZwU3U'  # Votre clé d'accès Unsplash
    url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={access_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ceci va lever une exception pour les réponses d'erreur
        results = response.json()['results']
        if results:
            # Retourne l'URL de la première image trouvée
            return results[0]['urls']['regular']
    except requests.RequestException as e:
        print(f"Erreur lors de la requête à l'API Unsplash: {e}")
    return None

# Exemple d'utilisation
image_url = fetch_unsplash_image('shoes')
print(image_url)
