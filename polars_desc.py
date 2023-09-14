""" A python script that does data analysis using polars dataframes """

import polars as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


def read_data(path):
    """
    Read the data from the path specified.
    """
    return pl.read_csv(path, try_parse_dates=True)


def plot_returns(ccy_df, column="Close"):
    """takes data from a polars dataframe and plots the returns"""
    fig, ax = plt.subplots()
    tickers = ccy_df["Instrument"].unique()
    for ccy in tickers:
        df = ccy_df.filter(
            (pl.col("Instrument") == ccy) & (pl.col("Price type") == column)
        )
        ax.plot(df["Datetime"], df["Price"].pct_change().cumsum())
        pass
    plt.legend(tickers)
    ax.set_ylabel("% change")
    ax.set_xlabel("Date")
    plt.xticks(rotation=45)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d%b"))
    plt.locator_params(axis="x", nbins=5)
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
    fig.suptitle("Currency returns")
    pass
