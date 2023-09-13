import ccy_library


def create_ticker(ccy):
    ticker = ccy.upper() + "=X"
    return ticker


def plot_returns(
    ccy_list=None, ccy_dict=None, column="Close", time_period=30
):  # adapt this function to dfs
    """It generates a plot of the currencies given.
    1 - If ccy_list is given, data will be downloaded for every currency in the list.
    2 - If ccy_dict is given, plots will be generated for every currency in dict.keys
    """
    if type(ccy_list) == str:
        ccy_dict = create_currencies_dict(ccy_list, date_range(time_period=time_period))
        pass
    if type(ccy_list) == list:
        ccy_dict = create_currencies_dict(ccy_list, date_range(time_period=time_period))
    df = pd.DataFrame(columns=ccy_dict.keys())
    for i in df.columns:
        df[i] = ccy_dict[i][column]
        pass
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


def print_range(ccy_df):  # adapt this code with multiindex headers?
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


# adapt this function to create single currency df
def create_df(ccy, ccy_dict):
    df = pd.DataFrame(ccy_dict[ccy])
    df.name = ccy
    return df
