class Car:
    def __init__(self, make, model, fuel_type, colour, fuel_level, mileage=0, fuel_capacity=100):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.colour = colour
        self.fuel_level = fuel_level
        self.mileage = mileage
        self.fuel_capacity = fuel_capacity

    def get_mileage(self):
        return self.mileage

    def get_fuel_level(self):
        return self.fuel_level

    def set_fuel_level(self, new_fuel_level):
        self.fuel_level = new_fuel_level

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_colour(self):
        return self.colour

    def set_colour(self, new_colour):
        self.colour = new_colour

    def display_car_details(self):
        print(f"Car Details:\n  Make: {self.make}\n  Model: {self.model}\n  Colour: {self.colour}\n  Fuel Type: {self.fuel_type}\n  Fuel Level: {self.fuel_level:.2f}\n  Mileage: {self.mileage:.2f}")

    def drive(self, distance):
        if distance <= 0:
            print("Invalid distance. Please enter a positive value.")
            return

        fuel_used = distance / 10  # 10 miles per fuel unit
        if self.fuel_level < fuel_used:
            print("Not enough fuel to drive that distance. Please fill up fuel.")
            return

        self.mileage += distance
        self.fuel_level -= fuel_used
        print(f"Drove {distance:.2f} miles. Current fuel level: {self.fuel_level:.2f}")

    def fill_fuel(self, amount):
        if amount <= 0:
            print("Invalid fuel amount. Please enter a positive value.")
            return

        if self.fuel_level + amount > self.fuel_capacity:
            print(f"Cannot add that much fuel. Fuel capacity is {self.fuel_capacity:.2f} units. Topping off the fuel tank.")
            self.fuel_level = self.fuel_capacity
        else:
           self.fuel_level += amount
        print(f"Added {amount:.2f} fuel units. Current fuel level: {self.fuel_level:.2f}")


def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_string_input(prompt):
    while True:
      value = input(prompt)
      if value:
        return value
      else:
        print("Invalid input. Please enter a value.")


def create_car_from_user():
    print("Let's create your car!")
    make = get_valid_string_input("Enter the car make: ")
    model = get_valid_string_input("Enter the car model: ")
    fuel_type = get_valid_string_input("Enter the fuel type (e.g., gasoline, electric): ")
    colour = get_valid_string_input("Enter the car colour: ")
    fuel_level = get_valid_float_input("Enter initial fuel level: ")
    fuel_capacity = get_valid_float_input("Enter the fuel capacity of the car")
    return Car(make, model, fuel_type, colour, fuel_level, fuel_capacity=fuel_capacity)


def main():
    my_car = create_car_from_user()

    while True:
        print("\nWhat would you like to do?")
        print("1. Get Car Details")
        print("2. Get Mileage")
        print("3. Get Fuel Level")
        print("4. Set Fuel Level")
        print("5. Drive")
        print("6. Fill Fuel")
        print("7. Change Colour")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            my_car.display_car_details()
        elif choice == "2":
            print(f"Mileage: {my_car.get_mileage():.2f}")
        elif choice == "3":
            print(f"Fuel Level: {my_car.get_fuel_level():.2f}")
        elif choice == "4":
            new_level = get_valid_float_input("Enter new fuel level: ")
            my_car.set_fuel_level(new_level)
            print("Fuel level updated!")
        elif choice == "5":
            distance = get_valid_float_input("Enter distance to drive: ")
            my_car.drive(distance)
        elif choice == "6":
            fuel_amount = get_valid_float_input("Enter fuel amount to add: ")
            my_car.fill_fuel(fuel_amount)
        elif choice == "7":
            new_colour = get_valid_string_input("Enter the new car colour: ")
            my_car.set_colour(new_colour)
            print("Car colour updated!")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
