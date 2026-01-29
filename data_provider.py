import yfinance as yf

def get_prices(asset, start_date, end_date):
    data = yf.download(asset, start=start_date, end=end_date)
    prices = data["Close"].values.flatten().tolist()
    return prices
