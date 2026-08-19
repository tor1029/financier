#this is for extracting historical returns
import yfinance as yf
#yahoo finance
import pandas as pd
#data analysis library
from yfinance import EquityQuery
#stock screener
from pprint import pprint
#do pprint(etc) so things stack nicely if u want, only for output looks
#--------------------------------------------------------------------------------------

stock = yf.Ticker("AAPL")
#can also do indices like spy, and add .fundsdata.(more stuff that will have a dropdown)
time = stock.history(period = '10y') #max for full
#all types of yf.(calendars(economic_calendar, etc))
#--------------------------------------------------------------------------------------

SCREENER CODE 
q = EquityQuery(
    'and', [
        EquityQuery('eq', ['region', 'us']),
        EquityQuery('gt',['percentchange', 10]),
        EquityQuery('eq',['exchange', 'NYQ'])
    ]
)
screen = yf.screen(q, sortField='percentchange', sortAsc=False)
for q in screen['quotes']:
    print(q['symbol'], q.get('displayName'), q.get('regularMarketChangePercent'))
#--------------------------------------------------------------------------------------

#PRINTING STOCK INFO 31-34
print(stock.info['forwardPE'])
#to see all .info, just print stock.info no brackets
#.news, .calendar, 
#--------------------------------------------------------------------------------------

#OPTIONS STUFF
#stock.options for expiry, stock.option_chain(stock.options[0]).calls to see calls on the first listed expiry
#---------------------------------------------------------------------------------------

#VARIABLES FOR DOWNLOADING CSV OF RETURNS
#time = time[['Close']]
#time.to_csv("AAPLReturns.csv")
#-------------------------------------------------------------------------------------------

#JUST SERVES AS A CHECKER TO SEE WHEN THE DATA STARTED/STOPPED
#print(time.head())
#print(time.tail())

#LIVE DATA
#ws = yf.WebSocket()
#ws.subscribe(['AAPL'])
#ws.listen(print)