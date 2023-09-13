import yfinance as yf


def download_prices_1y(tickers):
    data = yf.download(tickers, interval="1y")
    data.to_csv("currency_prices.csv")
