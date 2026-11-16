#Prompt for Input: Write a main() function that prompts the user for four inputs: a ticker symbol (string), a sector name (string), a P/E ratio (float), and a 95% VaR percentage (float). 
#Format the string inputs to strip whitespace and standardize capitalization.
#Sector Categorization (match): Implement a match statement that evaluates the inputted sector. i used if else instead bc it just makes more sense
#If "Technology" or "Consumer Discretionary", assign a risk variable to "High".
#If "Financials" or "Industrials", assign it to "Moderate".
#If "Consumer Staples" or "Utilities", assign it to "Low".

#Quantitative Filter (bool): Define a separate function called is_viable(pe, var) that returns a Boolean. It must return True if the P/E ratio is 18.0 or lower AND the VaR is 5.0 or lower.
    # It must return False otherwise. (Write this pythonically by returning the Boolean expression itself).
#Execution Logic (if/elif/else): Back in main(), call your is_viable function. Construct an if/elif/else block that evaluates both the boolean result and the sector risk variable to print a final recommendation:
#Print a "Strong Buy" message if the asset is viable AND the sector risk is Low.
#Print a "Buy" message if the asset is viable AND the sector risk is Moderate or High.
#Print a "Strong Sell" message if the asset is NOT viable AND the sector risk is High.
#Print a "Hold/Pass" message for all other conditions.



def is_viable(pe, var):
    if pe <= 18.0 and var <= 5.0:
        return True

def main():
    sectors = ["Consumer Staples", "Utilities", "Financials", "Industrials", "Technology", "Consumer Discretionary"]
    ticker = str(input("Input your ticker of choice: ")).strip().upper()
    
    while True:
        sector = str(input("Input the sector of the ticker: ")).title()
        if sector in sectors:
          break
        print(f"Invalid sector. Please refer to the list: \n {sectors}")
    pe = float(input("Please input the P/E Ratio (ex. 12.23): "))
    var = float(input("Please input the Value at Risk at 95% confidence (eg. 5.0): "))

    if is_viable(pe,var):
        if sector in ["Consumer Staples", "Utilities"]:
            print(f"{ticker} is a Strong Buy")
        else:
            print(f"{ticker} is a Buy")
    else:
        if sector not in ["Technology", "Consumer Discretionary"]:
            print(f"{ticker} is a Hold or Pass")
        else:
            print(f"{ticker} is a Strong Sell")

    


if __name__ == "__main__":
    main()