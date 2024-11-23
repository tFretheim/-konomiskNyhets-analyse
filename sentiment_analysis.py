from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(news_data):
    analyzer = SentimentIntensityAnalyzer()
    for article in news_data:
        sentiment_score = analyzer.polarity_scores(article['title'])
        article['sentiment'] = sentiment_score['compound']  # Sentiment score (-1 to 1)
    
    return news_data
