import yfinance as yf
#yahoo finance
import matplotlib.pyplot as plt
#this is for graphs whatnot
import pandas as pd
#data
import numpy as np
#helps w/ speed
from scipy.optimize import minimize
#make sure to download scipy 'python -m pip install scipy'
#scipy is equation library, minimize = import a highly versatile tool used to find the lowest possible value (the minimum) of a mathematical equation.
from datetime import datetime

#downloading the data
tickers = ["NVDA", 'MSFT', 'EFX', 'GLD', 'TPL', 'TSLA', 'VOO']
data = yf.download(tickers, start='2016-01-01', end = (datetime.today()))

#nitty gritty for monte carlo