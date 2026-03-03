# ------------------------------
# Stock Portfolio Tracker
# ------------------------------

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 3500
}

total_investment = 0
portfolio = {}

print("=================================")
print("     📈 STOCK PORTFOLIO TRACKER  ")
print("=================================")
print("Available Stocks and Prices:")
print(stock_prices)
print()

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {quantity} shares of {stock_name}")
        print()
    else:
        print("❌ Stock not available in price list.\n")

# Display Portfolio Summary
print("\n========= PORTFOLIO SUMMARY =========")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    print(f"{stock} - {quantity} shares × ${price} = ${investment}")

print("--------------------------------------")
print("Total Investment Value: $", total_investment)

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("--------------------------\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} - {quantity} shares × ${price} = ${investment}\n")
    file.write("--------------------------\n")
    file.write(f"Total Investment Value: ${total_investment}")


print("\n✅ Portfolio saved to 'portfolio_summary.txt'")
