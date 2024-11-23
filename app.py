import streamlit as st
from scraper import get_news
from sentiment_analysis import analyze_sentiment
from market_data import get_stock_data
from visualizations import visualize_data

def display_dashboard():
    # Fetch news data
    news_data = get_news()  # This will fetch news articles

    # Perform sentiment analysis
    news_data_with_sentiment = analyze_sentiment(news_data)  # Pass the news data to sentiment analysis
    
    # Fetch stock market data (you can change the ticker symbol if needed)
    stock_data = get_stock_data()

    # Check if stock_data is empty
    if stock_data.empty:
        st.error("No stock data found. Please check the stock symbol or data source.")
        return  # Exit early if there's no valid stock data
    
    # Display news and sentiment
    st.title('Økonomiske Nyheter og Markedsdata')

    st.subheader('Økonomiske Nyheter')
    for article in news_data_with_sentiment:
        st.write(f"**{article['title']}** - Sentiment: {article['sentiment']}")
        st.write(f"[Les mer]({article['link']})")

    # Display stock data in a chart
    st.subheader('Aksjekurs for Apple')
    st.line_chart(stock_data['Close'])
    
    # Visualizations for both sentiment and stock data
    visualize_data(stock_data, news_data_with_sentiment)

# Run the Streamlit app
if __name__ == "__main__":
    display_dashboard()
