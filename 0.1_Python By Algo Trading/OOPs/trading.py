class tradingStrategy:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        self.position = 0

    def buy(self, price, quantity):
        if self.amount >= price * quantity:
            self.position += quantity
            self.amount -= price * quantity
            print(f"successfully bought {quantity} of {self.symbol} at ${price}")
        else:
            print("Insufficient funds to buy")

    def sell(self, price, quantity):
        if self.position >= quantity:
            self.position -= quantity
            self.amount += price * quantity
            print(f"successfully sold {quantity} of {self.symbol} at ${price}")
        else:
            print("Insufficient position to sell")

    def status(self):
        print(f"current position {self.position} of shares")
        print(f"remaining amount ${self.amount}")


# ---------------- MAIN PROGRAM ----------------
symbol = input("Enter the stock symbol: ")
amount = float(input("Enter the initial amount: "))

trade = tradingStrategy(symbol, amount)

while True:
    print("\nTrading Menu:")
    print("1. Buy")
    print("2. Sell")
    print("3. Status")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        price = float(input("Enter the price to buy: "))
        quantity = int(input("Enter the quantity to buy: "))
        trade.buy(price, quantity)

    elif choice == 2:
        price = float(input("Enter the price to sell: "))
        quantity = int(input("Enter the quantity to sell: "))
        trade.sell(price, quantity)

    elif choice == 3:
        trade.status()

    elif choice == 4:
        print("Exiting the trading system Thank you.")
        break

    else:
        print("Invalid choice. Please try again.")
