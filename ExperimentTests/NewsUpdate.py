import requests



def get_latest_news(api_key, query="top-headlines", country="ua"):
    url = f"https://newsapi.org/v2/{query}?country={country}&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Published: {article['publishedAt']}")
            print(f"URL: {article['url']}")
            print(f"Description: {article['description']}\n")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message')}")

# Replace with your NewsAPI key
API_KEY = "772e85f1da4e4436b1cc0722f56a82a0"
get_latest_news(API_KEY)