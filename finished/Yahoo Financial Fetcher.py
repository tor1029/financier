#this is for extracting historical returns
import yfinance as yf
#yahoo finance
import pandas as pd
#data analysis library
from yfinance import EquityQuery
#stock screener
from pprint import pprint
#do pprint(etc) so things stack nicely if u want, only for output looks
upper = 'False'
while upper == 'False':
    pick = input('INPUT TICKER IN ALL CAPS: ')
    if pick.isupper():
        upper = 'True'
    else:
        continue
good = 'False'
korq = ''
freq = input('quarterly or annually?')
while good != 'True':
    if 'q' or 'Q' in freq:
        good = 'True'
        korq = ' quarterly'
        stock = yf.Ticker(pick)
        income = stock.quarterly_financials
        balance = stock.quarterly_balance_sheet
        cash = stock.quarterly_cashflow
    elif 'n' or 'N' in freq:
        good = 'True'
        korq = ' annual'
        stock = yf.Ticker(pick)
        income = stock.financials
        balance = stock.balance_sheet
        cash = stock.cashflow
    else:
        continue
income.to_csv(pick + korq + ' IS.csv')
balance.to_csv(pick + ' BS.csv')
cash.to_csv(pick + korq + ' CF.csv')