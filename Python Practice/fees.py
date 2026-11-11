

def parse_currency(prices: str) -> float:
    return float(prices.strip().lstrip('$')) #removed any dollar sign or spaces and returns as a float instead of a string

def parse_percentage(rate: str) -> float:
    return float(rate.strip().rstrip('%')) #removes any '%' symbol and white space and returns as a float instead of a string

def calculate_net_cost(shares, prices, rate, commission=1.00):
    net = (shares * prices * rate) + commission #Calculates gross cost (shares * price), fee amount (gross * fee_rate), and returns total net cost (gross + fees + commission).
    print(f"The net cost of this trade is ${net:.2f}")

def main():
    ticker = str(input("Input your ticker: ")).upper() # 1. Ticker symbol (str)
    shares = int(input("How many shares?: ")) # 2. Number of shares (int)
    prices = str(input("What is the execution price per share? e.g '$150.25': "))  # 3. Execution price per share (str, e.g., "$150.25")
    rate = str(input("What is the exchange rate fee? e.g. '0.05%': ")) # 4. Exchange fee rate (str, e.g., "0.05%")
    
    prices = parse_currency(prices)
    rate = parse_percentage(rate)
    calculate_net_cost(shares, prices, rate)

if __name__ == "__main__":
    main()
