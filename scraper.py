import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://www.bloomberg.com/europe"  # Endre til ønsket økonominyhetsside
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Hent artikkeloverskrifter og lenker
    articles = soup.find_all('a', class_='story-package-module__story__link')
    news_data = []
    
    for article in articles:
        title = article.get_text()
        link = article['href']
        news_data.append({'title': title, 'link': link})
    
    return news_data

# Test web scraping
news = get_news()
for article in news:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print('-' * 80)
