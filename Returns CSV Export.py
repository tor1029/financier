#this is for extracting historical returns
import yfinance as yf

stock = yf.Ticker("AAPL")
time = stock.history(start = "2018-01-01", interval="1d")

time = time[['Close']]
time.to_csv("AAPLReturns.csv")

print(time.head())
print(time.tail())