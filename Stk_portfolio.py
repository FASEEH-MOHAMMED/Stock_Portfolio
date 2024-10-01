#portfolio task

portfolio = {}

def add_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity
    print(f"Added {quantity} shares of {symbol}.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print("Stock not found.")

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for symbol, quantity in portfolio.items():
            print(f"{symbol}: {quantity} shares")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            remove_stock(symbol)
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
