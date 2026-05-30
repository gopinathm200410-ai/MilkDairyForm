# mini project MILK DIARY

import time

class MilkDiary:

    # --------------------------
    # Constructor
    # --------------------------

    def __init__(self):

        self.products = {
            "milk": {"stock": 0, "price": 0},
            "curd": {"stock": 0, "price": 0},
            "buttermilk": {"stock": 0, "price": 0}
        }

        self.sales_history = []

    # --------------------------
    # Set Product Prices
    # --------------------------

    def set_prices(self):

        print("\n--- SET PRODUCT PRICES ---")

        for product in self.products:

            price = int(input(f"Enter price of {product}: "))

            self.products[product]["price"] = price

        print("\nPrices Updated Successfully!")

    # --------------------------
    # Import Stock (Milk In)
    # --------------------------

    def import_stock(self):

        print("\n--- IMPORT STOCK ---")

        for product in self.products:

            qty = int(input(f"Enter quantity of {product} to add: "))

            self.products[product]["stock"] += qty

        print("\nStock Imported Successfully!")

    # --------------------------
    # View Inventory
    # --------------------------

    def view_inventory(self):

        print("\n===================================")
        print("         CURRENT INVENTORY")
        print("===================================")

        for product, data in self.products.items():

            print(product.upper(),
                  "| Stock:", data["stock"],
                  "| Price:", data["price"])

        print("===================================\n")

    # --------------------------
    # Sell Product (Export)
    # --------------------------

    def sell_product(self):

        print("\n--- SELL PRODUCTS ---")

        total_bill = 0
        bill_details = []

        while True:

            product = input("Enter product (milk/curd/buttermilk or 'stop'): ")

            if product == "stop":
                break

            if product not in self.products:
                print("Invalid Product!")
                continue

            qty = int(input("Enter quantity: "))

            if qty > self.products[product]["stock"]:
                print("Not enough stock!")
                continue

            price = self.products[product]["price"]

            cost = qty * price

            self.products[product]["stock"] -= qty

            total_bill += cost

            bill_details.append(
                f"{product} x {qty} = {cost}"
            )

            print("Added to bill!")

        print("\nGenerating Bill...")
        time.sleep(1)

        print("\n========== BILL ==========")

        for item in bill_details:
            print(item)

        print("-------------------------")
        print("TOTAL BILL:", total_bill)
        print("=========================\n")

        self.save_sales(bill_details, total_bill)

    # --------------------------
    # Save Sales to File
    # --------------------------

    def save_sales(self, bill_details, total):

        file = open("sales_report.txt", "a")

        file.write("\nNEW SALE\n")

        for item in bill_details:
            file.write(item + "\n")

        file.write("TOTAL: " + str(total) + "\n")

        file.write("----------------------\n")

        file.close()

        print("Sales saved to file!")

    # --------------------------
    # Add Single Stock (Manual Import)
    # --------------------------

    def add_stock(self):

        product = input("Enter product name: ")

        if product not in self.products:
            print("Invalid Product")
            return

        qty = int(input("Enter quantity: "))

        self.products[product]["stock"] += qty

        print("Stock updated!")

    # --------------------------
    # Product Summary
    # --------------------------

    def summary(self):

        total_value = 0

        print("\n--- STOCK VALUE SUMMARY ---")

        for product, data in self.products.items():

            value = data["stock"] * data["price"]

            total_value += value

            print(product, "value:", value)

        print("TOTAL INVENTORY VALUE:", total_value)

    # --------------------------
    # Menu System
    # --------------------------

    def menu(self):

        while True:

            print("\n===================================")
            print("        MILK DIARY SYSTEM")
            print("===================================")

            print("1. Set Prices")
            print("2. Import Stock")
            print("3. Add Single Stock")
            print("4. View Inventory")
            print("5. Sell Product")
            print("6. Stock Value Summary")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.set_prices()

            elif choice == "2":
                self.import_stock()

            elif choice == "3":
                self.add_stock()

            elif choice == "4":
                self.view_inventory()

            elif choice == "5":
                self.sell_product()

            elif choice == "6":
                self.summary()

            elif choice == "7":
                print("Exiting Milk Diary System...")
                break

            else:
                print("Invalid Choice!")


# --------------------------
# MAIN PROGRAM
# --------------------------

print("===================================")
print("   WELCOME TO MILK DIARY SYSTEM")
print("===================================")

system = MilkDiary()
system.menu()