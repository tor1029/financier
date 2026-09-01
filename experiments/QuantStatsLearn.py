# %%
import quantstats as qs
import pandas as pd
import yfinance as yf

# %%
rets = qs.utils.download_returns('AAPL')
benchmark = qs.utils.download_returns('SPY')

# %%
qs.stats.sharpe(rets)

# %%
qs.stats.max_drawdown(rets)

# %%
qs.stats.value_at_risk(rets)

# %%
qs.stats.greeks(rets, benchmark).to_dict()

# %%
qs.plots.snapshot(rets)

# %%
qs.plots.montecarlo(rets.tail(504), sims=1000)

# %%
qs.reports.html(rets, benchmark, title='AAPL vs SP500', output='reportaapl.html')

# %%
por = {'AAPL': .5, 'MSFT': .5}

poret = pd.DataFrame({
    ticker: qs.utils.download_returns(ticker) for ticker in por
}).dropna()

port = (poret * pd.Series(por)).sum(axis=1).rename('Portfolio')
sp = qs.utils.download_returns('SPY').rename('SP500')


# %%
qs.reports.html(port, sp, output='portfolioreport.html', title='port vs market')

# %%



