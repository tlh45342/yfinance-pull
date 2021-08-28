import yfinance as yf
import pandas

data = yf.download (  
         tickers = "LC",
         period = "1d",
         interval = "1m",
         group_by = 'ticker',
         progress = False
       )

out = {}
df1 = pandas.DataFrame(out, columns = ['Datetime', 'Open', 'High', 'Low','Close','Adj Close','Volume'])  

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
      df1 = df1.append(bar,ignore_index=True)

fname = r"M:\data\out.csv"
print("Writing: ", fname)
df1.to_csv (fname, index = False, header=True)