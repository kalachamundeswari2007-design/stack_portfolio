# ==========================================
# CODEALPHA TASK 2
# STOCK PORTFOLIO TRACKER
# ==========================================

import csv

# ==========================================
# HARDCODED STOCK PRICES
# ==========================================

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

# Store user's portfolio
portfolio = {}

print("=" * 60)
print("              STOCK PORTFOLIO TRACKER")
print("=" * 60)

# ==========================================
# DISPLAY AVAILABLE STOCKS
# ==========================================

print("\nAvailable Stocks:")
print("-" * 30)

for stock, price in stock_prices.items():
    print(f"{stock:<10} : ${price:.2f}")

print("-" * 30)

# ==========================================
# GET STOCK DETAILS FROM USER
# ==========================================

while True:

    stock_name = input(
        "\nEnter stock name (or type 'done' to finish): "
    ).upper().strip()

    # Stop entering stocks
    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        print(
            "Please choose from:",
            ", ".join(stock_prices.keys())
        )
        continue

    # Get quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

    except ValueError:
        print("❌ Please enter a valid whole number.")
        continue

    # Get stock price
    price = stock_prices[stock_name]

    # ==========================================
    # HANDLE DUPLICATE STOCKS
    # ==========================================

    if stock_name in portfolio:

        portfolio[stock_name]["quantity"] += quantity

    else:

        portfolio[stock_name] = {
            "price": price,
            "quantity": quantity
        }

    # Calculate investment
    investment = (
        portfolio[stock_name]["price"]
        * portfolio[stock_name]["quantity"]
    )

    print(f"\n✅ {stock_name} added successfully!")
    print(f"Stock Price : ${price:.2f}")
    print(f"Quantity    : {quantity}")
    print(f"Investment  : ${price * quantity:.2f}")


# ==========================================
# CALCULATE TOTAL INVESTMENT
# ==========================================

total_investment = 0

for stock, details in portfolio.items():

    investment = (
        details["price"]
        * details["quantity"]
    )

    details["investment"] = investment

    total_investment += investment


# ==========================================
# DISPLAY PORTFOLIO
# ==========================================

print("\n")
print("=" * 70)
print("                         YOUR PORTFOLIO")
print("=" * 70)

if len(portfolio) == 0:

    print("No stocks were added.")

else:

    print(
        f"{'Stock':<12}"
        f"{'Price':<15}"
        f"{'Quantity':<12}"
        f"{'Investment':<15}"
    )

    print("-" * 70)

    for stock, details in portfolio.items():

        print(
            f"{stock:<12}"
            f"${details['price']:<14.2f}"
            f"{details['quantity']:<12}"
            f"${details['investment']:<14.2f}"
        )

    print("-" * 70)

    print(
        f"{'Total Investment:':<39}"
        f"${total_investment:.2f}"
    )

print("=" * 70)


# ==========================================
# SAVE RESULT
# ==========================================

if len(portfolio) > 0:

    save_file = input(
        "\nDo you want to save the result? (yes/no): "
    ).lower().strip()

    # ======================================
    # SAVE AS TXT
    # ======================================

    if save_file == "yes":

        with open(
            "portfolio_result.txt",
            "w"
        ) as file:

            file.write(
                "STOCK PORTFOLIO TRACKER\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )

            for stock, details in portfolio.items():

                file.write(
                    f"Stock       : {stock}\n"
                )

                file.write(
                    f"Price       : "
                    f"${details['price']:.2f}\n"
                )

                file.write(
                    f"Quantity    : "
                    f"{details['quantity']}\n"
                )

                file.write(
                    f"Investment  : "
                    f"${details['investment']:.2f}\n"
                )

                file.write(
                    "-" * 50 + "\n"
                )

            file.write(
                f"\nTotal Investment: "
                f"${total_investment:.2f}\n"
            )

        print(
            "\n✅ TXT file saved successfully!"
        )

        print(
            "File created: portfolio_result.txt"
        )

        # ==================================
        # SAVE AS CSV
        # ==================================

        with open(
            "portfolio_result.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock",
                "Price",
                "Quantity",
                "Investment"
            ])

            for stock, details in portfolio.items():

                writer.writerow([
                    stock,
                    f"{details['price']:.2f}",
                    details["quantity"],
                    f"{details['investment']:.2f}"
                ])

            writer.writerow([
                "",
                "",
                "Total",
                f"{total_investment:.2f}"
            ])

        print(
            "✅ CSV file saved successfully!"
        )

        print(
            "File created: portfolio_result.csv"
        )

    elif save_file == "no":

        print("\nResult was not saved.")

    else:

        print(
            "\n❌ Please enter only yes or no."
        )

else:

    print(
        "\nNo portfolio data available to save."
    )


# ==========================================
# END PROGRAM
# ==========================================

print("\nThank you for using Stock Portfolio Tracker! 🚀")