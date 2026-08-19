# %%
#python -m pip install plotly
#python -m pip install PyPortfolioOpt

# %%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from pypfopt import EfficientFrontier, objective_functions
from pypfopt import black_litterman, risk_models
from pypfopt import BlackLittermanModel, plotting
from pypfopt import DiscreteAllocation

# %%
#create
holdings = ['NVDA', 'MSFT', 'TPL', 'EFX', 'TSLA'] 
    

# %%
#get data
portfolio = yf.download(holdings, start = '2016-01-01', end = '2026-08-17')['Close']
bench = yf.download('SPY', start = '2016-01-01', end = '2026-08-17')['Close']

# %%
#market caps
mcaps = {}
for t in holdings:
    stock = yf.Ticker(t)
    mcaps[t] = stock.info['marketCap']
mcaps

# %%
#calc sigma and delta to get implied market returns
#ledoit-Wolf: a statistical method used to fix noisy or unstable covariance matrices by shrinking sample values toward a structured target.
s = risk_models.CovarianceShrinkage(portfolio).ledoit_wolf()

delta = black_litterman.market_implied_risk_aversion(bench)
delta

# %%
#heatmap
sns.heatmap(s.corr(), cmap='coolwarm')

# %%
market_prior = black_litterman.market_implied_prior_returns(mcaps, delta, s)
market_prior.plot.barh(figsize=(10,5));
#how much are we gonna be compensated per risk; this alone does not integrate any assumptions from user

# %%
#do not need view on all
viewdict = {
    'TSLA':.17,
    'NVDA':.35,
    'MSFT':.3
}

bl = BlackLittermanModel(s, pi=market_prior, absolute_views=viewdict)

# %%
#look at is as a plausible range for standard deviation, again assumptions
intervals = [
    (-.12, .3),
    (.14, .64),
    (-.08, .4),
]

# %%
#up = upper band
variances = []
for lb, ub in intervals:
    sigma = (ub - lb)/2
    variances.append(sigma ** 2)

print(variances)
omega = np.diag(variances)


# %%
#shortcuts to find market implied prior
bl = BlackLittermanModel(s, pi='market', market_caps=mcaps, risk_aversion=delta, absolute_views=viewdict, omega=omega)

# %%
#posterior returns estimate
ret_bl = bl.bl_returns()

# %%
rets_df = pd.DataFrame([market_prior, ret_bl, pd.Series(viewdict)], index=['Prior', 'Posterior', 'Views']).T
rets_df

# %%
rets_df.plot.bar(figsize=(12,8));
#pltshow only if py not notebook
plt.show()
# %%
ef = EfficientFrontier(ret_bl, s)
ef.add_objective(objective_functions.L2_reg)
ef.max_sharpe()
weights = ef.clean_weights()
weights

# %%
from pypfopt.plotting import plot_weights

#max sharpe
ef = EfficientFrontier(ret_bl, s)
ef.add_objective(objective_functions.L2_reg)
ef.max_sharpe()
weights = ef.clean_weights()
weights

plot_weights(weights)
plt.title("Optimal Weightings Per Assumptions")
ef.portfolio_performance(verbose = True, risk_free_rate = .06)
#pltshow only if py not notebook
plt.show()

# %%



