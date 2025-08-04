# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker")

while True:
    stock = input("Enter stock symbol (e.g., AAPL) or 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optionally save to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    file_type = input("Choose file format - txt or csv: ").lower()
    filename = f"portfolio_summary.{file_type}"
    
    if file_type == "txt":
        with open(filename, "w") as f:
            f.write("Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}")
    elif file_type == "csv":
        import csv
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["", "", "Total", total_investment])
    else:
        print("⚠️ Unsupported file type. Skipping file save.")

    print(f"✅ Portfolio saved to {filename}")
else:
    print("📁 File save skipped.")
