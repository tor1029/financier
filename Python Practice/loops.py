# Objective:
# Demonstrate mastery of Python loops (while loops, for loops, and iterating over lists of dictionaries) by building a command-line tool that aggregates and screens daily asset returns.
# Requirements:
# 1. Initialize an empty list called 'portfolio' to store asset data.
# 2. Create a 'while' loop that continuously prompts the user to input a stock ticker symbol. 
# 3. If the user inputs "done" (or "DONE", "Done"), break out of the 'while' loop.
# 4. If a ticker is entered, prompt the user for that asset's daily return percentage (as a float).
# 5. Store the ticker and its return together as a dictionary, and append this dictionary to your 'portfolio' list.
# 6. After the 'while' loop terminates, create a 'for' loop to iterate through the 'portfolio' list.
# 7. For each dictionary in the list, print the ticker and its return in a formatted string.
# 8. Inside this 'for' loop, check if the absolute value of the return exceeds a certain threshold (e.g., 5.0%). If it does, append a "High Volatility Flag" to the printed output for that specific asset.
# """
# Phase 2: Sector Aggregation (Dictionary Iteration)
# 9. Before your loops begin, initialize an empty dictionary called 'sector_returns'.
# 10. Inside your initial 'while' loop, ask the user to input the sector for the asset (e.g., "Tech", "Energy", "Real Estate") in addition to the ticker and return.
# 11. As you collect the data, populate the 'sector_returns' dictionary: use the sector name as the key, and keep a running total of the returns for that sector as the value.
# 12. At the very end of your program, create a new 'for' loop that iterates through both the keys (sectors) and values (total returns) of your 'sector_returns' dictionary simultaneously.
# 13. Print a final summary report displaying each sector and its aggregated return. 

def main():
  
    portfolio = []
    sectors = ['Technology', 'Healthcare', 'Financials', 'Consumer Staples', 'Consumer Cyclical', 'Energy', 'Materials']
    sector_returns = {}
    sector_count = {}

    while True:
        select_stock = input("\nPlease input the ticker you would like to add to the portfolio. Type 'Done' when portfolio is complete.\nTicker: ")
        if select_stock == "Done":
            break
        else:
            daily_return = float(input(f"You have added {select_stock} to your portfolio. Please input {select_stock}'s daily return (%).\n{select_stock} Daily Return (%): "))
            while True:
                stock_sector = (input(f"You have added {select_stock} to your portfolio. Please input {select_stock}'s sector.\nChoose from: Technology, Healthcare, Financials, Consumer Staples, Consumer Cyclical, Energy, Materials\n{select_stock}'s Sector: "))
                if stock_sector in sectors:
                    break
                else:
                    print("Please input a valid sector.\n")
            details = {"Ticker": select_stock, "DAR": daily_return}
            if stock_sector not in sector_returns:
                sector_returns[stock_sector] = daily_return
                sector_count[stock_sector] = 1
            else:
                sector_returns[stock_sector] += daily_return
                sector_count[stock_sector] += 1   
            portfolio.append(details)
            

    for count, stock in enumerate(portfolio, start=1):
        print(f"Stock {count}: {stock['Ticker']}, Daily Return: {stock['DAR']}")

    for gic, ret in sector_returns.items():
        print(f"{gic}, Aggregate Return: {ret/sector_count[gic]}%")

main()