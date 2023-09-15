![Currencies](https://github.com/nogibjj/mini-project3-jcb/actions/workflows/ci-cd_actions.yml/badge.svg)
# Hourly data for diverse currencies

### IDS 706 mini-project 3

This project has a script that downloads hourly data for various currencies. 
Additionally, I've added a script that performs descriptive analysis of those currencies' performance.

### Here's an example that analyzes some key statistics in USDMXN, NZDUSD & EURUSD

We ran the analysis between Aug 14, 2023 and Sep 14, 2023 and observed the following:
EURUSD's current value is 1.07.
Between 14/Aug/23 and 14/Sep/23:
- EURUSD dropped -1.8%
- EURUSD reached a low of 1.07 on 07 Sep 23
- EURUSD reached a high of 1.1 on 14 Aug 23
- EURUSD had an average and standard deviation of 1.08 and 0.01 over the period.
shape: (9, 2)
┌────────────┬──────────┐
│ statistic  ┆ value    │
│ ---        ┆ ---      │
│ str        ┆ f64      │
╞════════════╪══════════╡
│ count      ┆ 549.0    │
│ null_count ┆ 0.0      │
│ mean       ┆ 1.082352 │
│ std        ┆ 0.007289 │
│ min        ┆ 1.069633 │
│ 25%        ┆ 1.074922 │
│ 50%        ┆ 1.082837 │
│ 75%        ┆ 1.088258 │
│ max        ┆ 1.09553  │
└────────────┴──────────┘
NZDUSD's current value is 0.59.
Between 14/Aug/23 and 14/Sep/23:
- NZDUSD dropped -0.65%
- NZDUSD reached a low of 0.59 on 05 Sep 23
- NZDUSD reached a high of 0.6 on 01 Sep 23
- NZDUSD had an average and standard deviation of 0.59 and 0.0 over the period.
shape: (9, 2)
┌────────────┬──────────┐
│ statistic  ┆ value    │
│ ---        ┆ ---      │
│ str        ┆ f64      │
╞════════════╪══════════╡
│ count      ┆ 550.0    │
│ null_count ┆ 0.0      │
│ mean       ┆ 0.593081 │
│ std        ┆ 0.003042 │
│ min        ┆ 0.58651  │
│ 25%        ┆ 0.590947 │
│ 50%        ┆ 0.592839 │
│ 75%        ┆ 0.595486 │
│ max        ┆ 0.600781 │
└────────────┴──────────┘
USDMXN's current value is 17.13.
Between 14/Aug/23 and 14/Sep/23:
- USDMXN rose 0.72%
- USDMXN reached a low of 16.68 on 28 Aug 23
- USDMXN reached a high of 17.71 on 07 Sep 23
- USDMXN had an average and standard deviation of 17.09 and 0.26 over the period.
shape: (9, 2)
┌────────────┬───────────┐
│ statistic  ┆ value     │
│ ---        ┆ ---       │
│ str        ┆ f64       │
╞════════════╪═══════════╡
│ count      ┆ 551.0     │
│ null_count ┆ 0.0       │
│ mean       ┆ 17.086869 │
│ std        ┆ 0.259848  │
│ min        ┆ 16.697901 │
│ 25%        ┆ 16.831409 │
│ 50%        ┆ 17.07259  │
│ 75%        ┆ 17.236    │
│ max        ┆ 17.693001 │
└────────────┴───────────┘
![Currency returns](https://github.com/nogibjj/mini-project3-JCB/blob/main/currency_returns.png)
