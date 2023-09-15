from polars_desc import read_data
from download_currencies import create_tickers, download_prices_long


def test_currencies():
    download_prices_long(create_tickers(["usdmxn"]))
    usdmxn = read_data("currency_prices_long.csv")
    assert usdmxn.shape[0] > 0
    assert "Datetime" in usdmxn.columns
