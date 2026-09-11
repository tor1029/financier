import matplotlib
matplotlib.use('Agg')  # Suppress matplotlib interactive popups
import matplotlib.pyplot as plt

import quantstats as qs
import pandas as pd
import yfinance as yf

# Loop to collect one or multiple tickers as separate strategies
rets_list = {}

collecting = True
while collecting:
    correct = False
    while not correct:
        pick = input("Input ticker: ").strip().upper()
        try:
            stock = yf.Ticker(pick)
            long_name = stock.info.get("longName") or pick
            confirm = input(f"{long_name}, does that look right? y or n: ").strip().lower()
            if "y" in confirm:
                correct = True
        except Exception as e:
            print(f"Invalid ticker or network error: {e}. Try again.")
            
    # Download and store returns with ticker as column name
    rets_list[pick] = qs.utils.download_returns(pick)
    
    # Prompt whether to add another ticker
    more = input("Would you like to add another ticker to this report? (y/n): ").strip().lower()
    if "y" not in more:
        collecting = False

# Combine all tickers into a multi-column DataFrame
rets_df = pd.DataFrame(rets_list)

# Keep SPY benchmark constant and explicitly name the series to avoid "Close" label bug
benchmark = qs.utils.download_returns("SPY")
benchmark.name = "SPY"

# Align indexes to prevent dimension/date mismatch errors across all columns and benchmark
aligned_data = pd.concat([rets_df, benchmark], axis=1, sort=False).dropna()
rets = aligned_data.iloc[:, :-1]  # All ticker columns
benchmark = aligned_data.iloc[:, -1]  # SPY column

ticker_names = list(rets.columns)
pick_label = "-".join(ticker_names)

# Quantitative metrics & Visualizations (rendered headlessly via Agg backend)
qs.plots.snapshot(rets)
qs.plots.montecarlo(rets.tail(504), sims=1000)
plt.close('all')  # Clear any active plot figures

# HTML Report generation showing each ticker independently against SPY
html_filename = f"{pick_label}_vs_SPY_Report.html"
qs.reports.html(
    rets, 
    benchmark, 
    title=f"{pick_label} vs SPY", 
    filename=html_filename
)

print(f"HTML report successfully generated and saved as: {html_filename}")