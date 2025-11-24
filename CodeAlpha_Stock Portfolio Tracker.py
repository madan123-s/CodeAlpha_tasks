# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0
portfolio = {}

print("Enter stock details (type 'done' to finish)\n")

while True:
    stock = input("Stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found in price list!")
        continue

    qty = int(input("Quantity: "))

    # Store quantity
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} × {price} = {value}")

print("\nTotal Investment Value:", total_investment)

# Optional file saving
save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    filename = "portfolio.txt"
    with open(filename, "w") as file:
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} × {price} = {value}\n")
        file.write(f"\nTotal Investment: {total_investment}\n")
    
    print("Saved to portfolio.txt")