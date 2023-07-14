import requests

def fetch_news(api_key):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "in",  # Replace with your desired country code
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        articles = data["articles"]
        for article in articles:
            title = article["title"]
            source = article["source"]["name"]
            print(f"{source}: {title}")
    else:
        print("Failed to fetch news:", data["message"])

# Replace 'YOUR_API_KEY' with your actual News API key
API_KEY = '202639f904c2451c8c5cacab6d94ded1'

fetch_news(API_KEY)