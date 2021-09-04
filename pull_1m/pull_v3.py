import yfinance as yf
import pandas
from datetime import datetime, timedelta

#%%

def pull_day(Symbol, Datestr):

  enddate = datetime.fromisoformat(Datestr)
  enddate += timedelta(days=1)
  
  data = yf.download (  
           tickers = Symbol,
           period = "1d",
           interval = "1m",
           group_by = 'ticker',
           progress = False,
           start=Datestr,
           end=enddate
          )

  out = {}
  df = pandas.DataFrame(out, columns = ['Datetime', 'Open', 'High', 'Low','Close','Adj Close','Volume'])  

  for index, row in data.iterrows():
      if row['Open'] is not None:
        date = {"Datetime": index}
        open = {"Open": row['Open']}
        high = {"High": row['High']}
        low = {"Low": row['Low']}
        close = {"Close": row['Close']}
        adjclose = {"Adj Close": row['Adj Close']}
        volume = {"Volume": row['Volume']}
        bar = {**date, **open, **high, **low, **close, **adjclose, **volume}
        df = df.append(bar,ignore_index=True)

  return(df)

# ------------------------------

#%%

fname = r"m:\data\tradepool.csv"
names = pandas.read_csv(fname,header=0,names=['Symbol'])
    
count = 0
daystr  = "2021-07-01"

for index,row in names.iterrows():
      symbol = row['Symbol']
      df = pull_day(symbol, daystr)
      count = count + 1
      fname = r"m:\data\1m\{}-{}.csv".format(symbol, daystr)
      print("Writing: ", fname)
      df.to_csv (fname, index = False, header=True)
  
print("Stocks:", count)