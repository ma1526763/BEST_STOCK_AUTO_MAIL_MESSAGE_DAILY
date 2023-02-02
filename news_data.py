import requests
import os

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

def get_news_data(STOCK_NAME):
    news_parameters = {
        "q": STOCK_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_data = requests.get(NEWS_API_ENDPOINT, params=news_parameters).json()["articles"][:3]
    news_to_send = "".join([f"News#{i + 1} Source: ({news['source']['name']})\nTitle: {news['title']}\n{news['description']}"
                            f"\nAuthor: {news['author']}\nRead more: {news['url']}\n\n" for i, news in enumerate(news_data)])
    return news_to_send
