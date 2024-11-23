import yfinance as yf

def get_stock_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="5m")  # Get data for the last day with 5-minute intervals
    
    if data.empty:
        print(f"Warning: No stock data found for {ticker}")
    
    return data
