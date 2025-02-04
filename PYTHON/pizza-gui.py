import sys
import tkinter as tk
from tkinter import ttk, messagebox

class PizzaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Order System")
        self.root.geometry("800x600")  # Adjusted size for better layout

        self.pizza = Pizza()  # Instantiate a Pizza object

        # Variables to store pizza details
        self.size_var = tk.StringVar()
        self.toppings_list = []  # List to store selected toppings
        self.delivery_var = tk.StringVar()

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="raised")
        self.style.configure("TLabel", padding=6)
        self.style.configure("TFrame", padding=10)

        # Frames for organization
        self.size_frame = ttk.Frame(self.root)
        self.size_frame.pack(pady=10)

        self.toppings_frame = ttk.Frame(self.root)
        self.toppings_frame.pack(pady=10)

        self.delivery_frame = ttk.Frame(self.root)
        self.delivery_frame.pack(pady=10)

        self.order_summary_frame = ttk.Frame(self.root)
        self.order_summary_frame.pack(pady=10)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # UI elements
        self.create_size_selection()
        self.create_toppings_selection()
        self.create_delivery_selection()
        self.create_order_summary()
        self.create_buttons()


    def create_size_selection(self):
        ttk.Label(self.size_frame, text="Choose Pizza Size:").pack()
        sizes = {"Small": 5.50, "Medium": 7.90, "Large": 12.00}
        for size, price in sizes.items():
            rb = ttk.Radiobutton(self.size_frame, text=f"{size} (+£{price:.2f})", variable=self.size_var, value=size,
                                command=self.update_pizza_size)  # Call update method
            rb.pack(anchor=tk.W)

    def update_pizza_size(self):
         selected_size = self.size_var.get()
         self.pizza.size = selected_size  # Update Pizza object's size
         sizes = {"Small": 5.50, "Medium": 7.90, "Large": 12.00}
         self.pizza.prize = sizes.get(selected_size, 0.0)  # Update price too, resetting it
         # Add back toppings prices
         for topping in self.toppings_list:
            self.pizza.prize += 0.75

         self.update_order_summary()

    def create_toppings_selection(self):
        ttk.Label(self.toppings_frame, text="Choose Toppings:").pack()
        self.topping_vars = {}
        toppings = {"Pepperoni": 0.75, "Mushrooms": 0.75, "Extra-cheese": 0.75, "Onions": 0.75,
                    "Sausage": 0.75, "Black-Olives": 0.75, "Green-pepper": 0.75, "Fresh-garlic": 0.75}

        for topping, price in toppings.items():
            var = tk.BooleanVar()
            self.topping_vars[topping] = var
            cb = ttk.Checkbutton(self.toppings_frame, text=f"{topping} (+£{price:.2f})", variable=var,
                                command=self.update_toppings) # call update method
            cb.pack(anchor=tk.W)


    def update_toppings(self):
        self.toppings_list = [topping for topping, var in self.topping_vars.items() if var.get()]  # Update list
        self.pizza.toppings = self.toppings_list
        # Recalculate price: Reset to size price and add topping prices.
        sizes = {"Small": 5.50, "Medium": 7.90, "Large": 12.00}
        self.pizza.prize = sizes.get(self.pizza.size, 0.0)

        for topping in self.toppings_list:
            self.pizza.prize += 0.75 # price for each topping is fixed.

        self.update_order_summary()

    def create_delivery_selection(self):
        ttk.Label(self.delivery_frame, text="Choose Delivery Option:").pack()
        deliveries = {"Flat rate slow": 3.75, "Flat rate fast": 7.50}

        for delivery, price in deliveries.items():
            rb = ttk.Radiobutton(self.delivery_frame, text=f"{delivery} (+£{price:.2f})", variable=self.delivery_var, value=delivery,
                                command=self.update_delivery)  #Call update method
            rb.pack(anchor=tk.W)

    def update_delivery(self):
        selected_delivery = self.delivery_var.get()
        deliveries = {"Flat rate slow": 3.75, "Flat rate fast": 7.50}
        delivery_price = deliveries.get(selected_delivery, 0.0)

        #First substract any existing delivery cost.
        if self.pizza.prize > 5 and self.pizza.size != None:
            if selected_delivery == 'Flat rate slow':
                self.pizza.prize -= 7.50 if self.pizza.prize > 7.50 else 0.00
            elif selected_delivery == 'Flat rate fast':
                 self.pizza.prize -= 3.75 if self.pizza.prize > 3.75 else 0.00

        if selected_delivery == 'Flat rate slow':
            self.pizza.prize += 3.75
        elif selected_delivery == 'Flat rate fast':
            self.pizza.prize += 7.50

        self.update_order_summary()

    def create_order_summary(self):
        self.summary_label = ttk.Label(self.order_summary_frame, text="Order Summary:\nNo items selected.")
        self.summary_label.pack()

    def update_order_summary(self):
        summary_text = "Order Summary:\n"
        if self.pizza.size:
            summary_text += f"Size: {self.pizza.size}\n"
        if self.pizza.toppings:
            summary_text += f"Toppings: {', '.join(self.pizza.toppings)}\n"
        if self.delivery_var.get():
            summary_text += f"Delivery: {self.delivery_var.get()}\n" #Get the delivery price
        summary_text += f"Price: £{self.pizza.prize:.2f}"

        self.summary_label.config(text=summary_text) # update text

    def create_buttons(self):
        ttk.Button(self.button_frame, text="View Order", command=self.view_order).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Checkout", command=self.checkout).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Exit", command=self.root.destroy).pack(side=tk.LEFT, padx=5)

    def view_order(self):
         self.update_order_summary() # Make sure the displayed order summary is updated.
         # The summary should already be updated via other actions.
         pass # Nothing to do here but display the current order


    def checkout(self):
        if self.pizza.size is None:
            messagebox.showinfo("Checkout", "Please select a pizza size before checking out.")
            return

        if self.pizza.prize == 0.0:
            messagebox.showinfo("Checkout", "Please select toppings/delivery options before checking out.")
            return


        messagebox.showinfo("Checkout", f"Thank you for your order!\nTotal: £{self.pizza.prize:.2f}")
        # Reset the pizza after checkout
        self.pizza = Pizza()
        self.size_var.set("")
        for topping in self.topping_vars:
            self.topping_vars[topping].set(False)

        self.toppings_list = []
        self.delivery_var.set("")
        self.update_order_summary()


class Pizza:
    def __init__(self, toppings=None, size=None, prize=0):
        self.toppings = toppings if toppings else []
        self.size = size
        self.prize = prize


def main():
    root = tk.Tk()
    gui = PizzaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
