import sys
from tkinter import Tk

class Pizza:
    def __init__(self, toppings=None, size=None, prize=0):
        self.toppings = toppings if toppings else []
        self.size = size
        self.prize = prize

    def display_menu(self):
        print("\nPizza Menu:")
        print("1. Choose Pizza Size")
        print("2. Add Toppings")
        print("3. Choose Delivery Option")
        print("4. View Pizza")
        print("5. Exit")

    def choose_size(self):
        print("\nAvailable Sizes:")
        print("1. Small (+$5.50)")
        print("2. Medium (+$7.90)")
        print("3. Large (+$12)")

        while True:
            size_choice = input("Enter your size choice (1-3): ")
            if size_choice == '1':
                self.size = "Small"
                self.prize += 5.50
                print("You have chosen a Small pizza.")
                break
            elif size_choice == '2':
                self.size = "Medium"
                self.prize += 7.90
                print("You have chosen a Medium pizza.")
                break
            elif size_choice == '3':
                self.size = "Large"
                self.prize += 12
                print("You have chosen a Large pizza.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def add_toppings(self):
        print("\nAvailable Toppings:")
        print("1. Pepperoni £0.75")
        print("2. Mushrooms £0.75")
        print("3. Extra-cheese £0.75")
        print("4. Onions £0.75")
        print("5. Sausage £0.75")
        print("6. Black-Olives £0.75")
        print("7. Green-pepper £0.75")
        print("8. Fresh-garlic £0.75")
        print("9. Done Adding Toppings")

        while True:
            topping_choice = input("Enter topping number (1-9): ")
            if topping_choice == '1':
                self.prize += 0.75
                self.toppings.append("Pepperoni")
                print("Pepperoni added.")
            elif topping_choice == '2':
                self.prize += 0.75
                self.toppings.append("Mushrooms")
                print("Mushrooms added.")
            elif topping_choice == '3':
                self.prize += 0.75
                self.toppings.append("Extra-cheese")
                print("Extra-cheese added.")
            elif topping_choice == '4':
                self.prize += 0.75
                self.toppings.append("Onions")
                print("Onions added.")
            elif topping_choice == '5':
                self.prize += 0.75
                self.toppings.append("Sausage")
                print("Sausage added")
            elif topping_choice == '6':
                self.prize += 0.75
                self.toppings.append("Black Olives")
                print("Black-Olives added")
            elif topping_choice == '7':
                self.prize += 0.75
                self.toppings.append("Green-pepper")
                print("Green-pepper added.")
            elif topping_choice == '8':
                self.prize += 0.75
                self.toppings.append("Fresh-garlic")
                print("Fresh-garlic added.")
            elif topping_choice == '9':
                break
            else:
                print("Invalid topping choice.")

    def view_pizza(self):
        print("\nYour Pizza:")
        if self.size:
            print(f"Size: {self.size}")
        else:
            print("No size selected.")

        if self.toppings:
            print("Toppings:", ", ".join(self.toppings))
        else:
            print("No toppings selected.")

        print(f"Price: £{self.prize:.2f}")

    def view_deli(self):
        print("What type of delivery you want?")
        print("1. Flat rate slow (£3.75)")
        print("2. Flat rate fast (£7.50)")
        print("3. Exit")
        while True:
            deli_choice = input("Enter number (1-3): ")
            if deli_choice == '1':
                self.prize += 3.75
                print("You have chosen a Flat rate slow.")
                break
            elif deli_choice == '2':
                self.prize += 7.50
                print("You have chosen a Flat rate fast.")
                break
            elif deli_choice == '3':
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


def start_demo():
    pizzas = []
    order_total = 0.0

    while True:
        print("\nOrder Menu:")
        print("1. Add a Pizza")
        print("2. View Order")
        print("3. Checkout")
        print("4. Exit")

        order_choice = input("Enter your choice: ")

        if order_choice == '1':
            pizza = Pizza()  
            while True:
                pizza.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    pizza.choose_size()
                elif choice == '2':
                    pizza.add_toppings()
                elif choice == '3':
                    pizza.view_deli()
                elif choice == '4':
                    pizza.view_pizza()
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
            pizzas.append(pizza)  
            print("Pizza added to order.")


        elif order_choice == '2':
            if not pizzas:
                print("No pizzas in the order yet.")
            else:
                print("\n--- Current Order ---")
                for i, pizza in enumerate(pizzas):
                    print(f"\nPizza #{i+1}:")
                    pizza.view_pizza()  
                order_total = sum(pizza.prize for pizza in pizzas)
                print(f"\nSubtotal: £{order_total:.2f}")


        elif order_choice == '3':
            if not pizzas:
                print("No pizzas in the order.  Please add pizzas before checking out.")
            else:
                order_total = sum(pizza.prize for pizza in pizzas)
                print(f"\n--- Checkout ---")
                print(f"Total: £{order_total:.2f}")
                print("Thank you for your order!")
                pizzas = [] 
                order_total = 0.0
                break

        elif order_choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start_demo()