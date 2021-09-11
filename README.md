# yfinance-pull
example code for pulling financial data using yfinance

The consisteance for Yahoo to report on 1M appears to be inconsistent.
I have found that at the end of the month I have been able to get all 30 days.
I have seen that intraweek I have only been able to go a few days back.

When you ask for data beyond what is available you will see something like....
- LC: No data found for this date range, symbol may be delisted

This a "test" project. 
The example piece does have the storage address hardcoded to drive M.
I run python on Windows, Linux, and Apple.
It is expected that you would alter the code to fit your environment.

The example files in pull_1M show a piece of code in a series of strages of development.

The file pull_v3.py uses a CSV file aptly named "tradingpool.csv" as the source for a series of downloads.

## INSTALLATION

```bash
git clone https://github.com/tlh45342/yfinance-pull.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```
