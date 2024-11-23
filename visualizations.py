import matplotlib.pyplot as plt

def visualize_data(stock_data, news_data):
    # Visualize stock prices
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data.index, stock_data['Close'], label="Aksjekurs", color='blue')
    plt.title('Aksjekurs for Apple')
    plt.xlabel('Tid')
    plt.ylabel('Pris (USD)')
    plt.legend()
    plt.show()

    # Visualize sentiment of news articles
    sentiments = [article['sentiment'] for article in news_data]
    titles = [article['title'][:40] + '...' for article in news_data]  # Shorten titles for display
    plt.figure(figsize=(10, 5))
    plt.barh(titles, sentiments, color='orange')
    plt.title('Sentimentanalyse av Økonomiske Nyheter')
    plt.xlabel('Sentimentverdi')
    plt.show()
