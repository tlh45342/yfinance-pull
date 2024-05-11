import yfinance as yf
import pandas
import warnings

#pandas is getting chatty when using concat 
warnings.simplefilter(action='ignore', category=FutureWarning)

data = yf.download (  
         tickers = "LC",
         period = "1d",
         interval = "1d",
         progress = False
       )

out = {}
df = pandas.DataFrame(out, columns = ['Datetime', 'Open', 'High', 'Low','Close','Adj Close','Volume'])  

for index, row in data.iterrows():
    if row['Open'] is not None:
      bar = pandas.DataFrame({"Datetime": [index],
                              "Open": [row['Open']],
                              "High": [row['High']],
                              "Low": [row['Low']],
                              "Close": [row['Close']],
                              "Adj Close": [row['Adj Close']],
                              "Volume": [row['Volume']]})
      df = pandas.concat([df, bar])

fname = "out.csv"
print("Writing: ", fname)
df.to_csv (fname, index = False, header=True)
