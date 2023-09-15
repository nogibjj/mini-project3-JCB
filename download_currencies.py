import yfinance as yf


def yf_ticker(ccy):
    ticker = ccy.upper() + "=X"
    return ticker


def create_tickers(ccy_list):
    tickers = [yf_ticker(ticker) for ticker in ccy_list]
    return tickers


def download_prices_long(tickers):
    data = yf.download(tickers, period="1mo", interval="60m")
    data.reset_index(inplace=True)
    data = data.melt(
        id_vars="Datetime", var_name=["Price type", "Instrument"], value_name="Price"
    )
    data.to_csv("currency_prices_long.csv")
    pass
