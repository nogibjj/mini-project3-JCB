import ccy_library
import matplotlib.pyplot as plt
from ccy_library import create_ticker


def plot_returns(ccy_df, column="Close"):
    df = ccy_df.loc[:, column]
    fig, ax = plt.subplots()
    for ccy in df.columns:
        ax.plot(df[ccy].pct_change())
        pass
    plt.legend(df.columns)
    ax.set_ylabel("% change")
    ax.set_xlabel("Date")
    plt.xticks(rotation=45)
    fig.suptitle("Currency returns")
    pass


def single_ccy_df(ccy_df, ccy):
    df = ccy_df.xs(create_ticker(ccy), level=1, axis=1)
    df.name = ccy
    return df


def print_range(ccy_df):
    low = ccy_df.Low.min()
    high = ccy_df.High.max()
    close = ccy_df.Close[-1]
    ccy_open = ccy_df.Open[0]
    average = ccy_df.Close.mean()
    std_dev = np.std(ccy_df.Close)
    print(ccy_df.name + "'s current value is {}.".format(round(close, 2)))
    print(
        "Between {} and {}:".format(
            ccy_df.index.min().strftime("%d/%b/%y"),
            ccy_df.index.max().strftime("%d/%b/%y"),
        )
    )
    print(
        "- "
        + ccy_df.name
        + " {} {}%".format(
            "dropped" if close < ccy_open else "rose",
            round((close / ccy_open - 1) * 100, 2),
        )
    )
    print(
        "- "
        + ccy_df.name
        + " reached a low of {} on {}".format(
            round(low, 2), ccy_df.index[ccy_df.Low == low][0].strftime("%d %b %y")
        )
    )
    print(
        "- "
        + ccy_df.name
        + " reached a high of {} on {}".format(
            round(high, 2), ccy_df.index[ccy_df.High == high][0].strftime("%d %b %y")
        )
    )
    print(
        "- "
        + ccy_df.name
        + " had an average and standard deviation of {} and {} over the period.".format(
            round(average, 2), round(std_dev, 2)
        )
    )
    pass
