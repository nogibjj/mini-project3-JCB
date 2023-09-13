import yfinance as yf
from ccy_library import create_ticker


def download_prices(tickers):
    data = yf.download(tickers, period="1mo", interval="60m")
    data.to_csv("currency_prices.csv")
    pass


def create_tickers(ccy_list):
    tickers = [create_ticker(ticker) for ticker in ccy_list]
    return tickers
