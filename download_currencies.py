import yfinance as yf
from ccy_library import create_ticker


def download_prices(tickers):
    data = yf.download(tickers, period="1mo", interval="60m")
    data.to_csv("currency_prices.csv")
    pass


def create_tickers(ccy_list):
    tickers = [create_ticker(ticker) for ticker in ccy_list]
    return tickers


def download_prices_long(tickers):
    data = yf.download(tickers, period="1mo", interval="60m")
    data.reset_index(inplace=True)
    data = data.melt(
        id_vars="Datetime", var_name=["Price type", "Instrument"], value_name="Price"
    )
    data.to_csv("currency_prices_long.csv")
    pass
