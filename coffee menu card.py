class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class CartItem:
    def __init__(self, coffee, quantity):
        self.coffee = coffee
        self.quantity = quantity

    def get_total(self):
        return self.coffee.price * self.quantity
class CoffeeShop:
    def __init__(self):
        self.menu = [
            Coffee("Espresso", 120),
            Coffee("Cappuccino", 150),
            Coffee("Latte", 180),
            Coffee("Americano", 130),
            Coffee("Mocha", 200)
        ]
    def show_menu(self):
        print("\n----- Coffee Menu -----")
        for index, coffee in enumerate(self.menu, start=1):
            print(f"{index}. {coffee.name} - Rs {coffee.price}")
    def get_valid_choice(self):
        while True:
            try:
                choice = int(input("\nEnter coffee number: "))
                if 1 <= choice <= len(self.menu):
                    return choice - 1
                else:
                    print("Please choose a valid coffee number.")
            except ValueError:
                print("Please enter a valid number.")
    def get_valid_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity cannot be zero or negative.")
            except ValueError:
                print("Please enter a valid number.")
    def take_order(self):
        print("\n===== Welcome to the Coffee Shop =====")
        customer_name = input("Enter your name: ")
        cart = []

        while True:
            self.show_menu()
            coffee_index = self.get_valid_choice()
            quantity = self.get_valid_quantity()

            selected_coffee = self.menu[coffee_index]
            cart_item = CartItem(selected_coffee, quantity)
            cart.append(cart_item)

            more = input("Do you want to add another coffee? (yes/no): ").strip().lower()
            if more != "yes":
                break

        self.generate_bill(customer_name, cart)
    def generate_bill(self, customer_name, cart):
        subtotal = 0

        print("\n----- Bill -----")
        print(f"Customer Name : {customer_name}")
        print("\nItems in Cart:")
        for item in cart:
            item_total = item.get_total()
            subtotal += item_total
            print(f"{item.coffee.name} x {item.quantity} = Rs {item_total:.2f}")

        gst = subtotal * 0.02
        total = subtotal + gst

        print(f"\nSubtotal      : Rs {subtotal:.2f}")
        print(f"GST (2%)      : Rs {gst:.2f}")
        print(f"Total Bill    : Rs {total:.2f}")
        print(f"\nThank you, {customer_name}!")
    def start(self):
        while True:
            self.take_order()
def main():
    shop = CoffeeShop()
    shop.start()
if __name__ == "__main__":
    main()