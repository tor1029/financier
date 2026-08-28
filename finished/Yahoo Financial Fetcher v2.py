#this is for extracting historical returns
import yfinance as yf
#yahoo finance
import pandas as pd
#data analysis libraryy
from yfinance import EquityQuery
#stock screener
from pprint import pprint
#do pprint(etc) so things stack nicely if u want, only for output looks
correct = False
while not correct:
    pick = input('Input ticker: ').strip().upper()
    stock = yf.Ticker(pick)
    confirm = input(f"{stock.info.get('longName')}, does that look right? y or n: ").strip().lower()
    if 'y' in confirm:
        correct = True
        continue
good = False
korq = ''
freq = input('quarterly or annually?: ').strip().lower()
while not good:
    if 'q' in freq:
        good = True
        korq = ' quarterly'
        income = stock.quarterly_financials
        balance = stock.quarterly_balance_sheet
        cash = stock.quarterly_cashflow
    elif 'n' in freq:
        good = True
        korq = ' annual'
        income = stock.financials
        balance = stock.balance_sheet
        cash = stock.cashflow
    else:
        continue
counter = 0
while counter < 1:
    inc = input('download income statement? y or n: ').strip().upper()
    if 'Y' in inc:
        income.to_csv(pick + korq + ' IS.csv')
        counter += 1
    
    bal = input('download balance sheet? y or n: ').strip().upper()
    if 'Y' in bal:
        balance.to_csv(pick + korq + ' BS.csv')
        counter += 1
    
    cf = input('download statement of cash flows? y or n: ').strip().upper()
    if 'Y' in cf:
        cash.to_csv(pick + korq + ' CF.csv')
        counter += 1
    
    if counter < 1:
        print()
        print("please select at least one statement to download")
        print()
print('download/s successful!')