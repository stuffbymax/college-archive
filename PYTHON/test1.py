import random
import time
import os

class Person:
    def __init__(self, age, name, Idnum):
        self.age = age
        self.name = name
        self.Idnum = Idnum

    def birthday(self):
        self.age = self.age + 1

    def get_idnum(self):
        return self.Idnum

    def set_idnum(self, new_idnum):
        self.Idnum = new_idnum
        
    def __str__(self): # added for better printing
        return f"Name: {self.name}, Age: {self.age}, ID: {self.Idnum}"
    
# Save the game state to a file
def save(people_list):
    with open("people.json", "w") as f:
        for person in people_list:
            f.write(f"{person.name},{person.age},{person.Idnum}\n")
    print("Saved successfully.")
    input("Press Enter to continue...")

def load():
    global people
    people = []  # Create an empty list to store loaded data
    if os.path.exists("people.json"):
        with open("people.json", "r") as f:
            for line in f:
                name, age, Idnum = line.strip().split(",")
                people.append(Person(int(age), name, Idnum))
        print("Loaded successfully.")
    else:
        print("No saved game found.")
    input("Press Enter to continue...")

        
# Store Person objects in a list
people = [
    Person(31, "Ben", "123456"),
    Person(42, "Paul", "987654"),
    Person(22, "Sarah", "456789"), 
    Person(60, "John", "789012"),
    Person(23, "johanson", "789014"),
    Person(21, "zdislav", "789016"),
    Person(21, "wladislav", "789024"),
    Person(22, "jakub", "789015"),
    Person(23, "gregosz", "789011"),
    Person(26, "Finn", "789112"),
    Person(25, "Marissa", "789212"),
    Person(23, "Jaxon", "789312"),
    Person(22, "Matej", "789412"),
    Person(19, "Ivana", "789512"),
    Person(17, "Ivan", "789612"),
    Person(17, "Zora", "789712"),
    Person(27, "Luke", "789812"),
    Person(22, "Boris", "789912"),
    Person(19, "Petra", "789992"),
    Person(17, "Pjotr", "789129")
]

# Initial print of the persons
for person in people:
  print(person)

while True:
    print("\nDo you want to update ID numbers?")
    print("Yes")
    print("No")
    print("save")
    print("load")

    choice = input("Enter your choice: ").lower()

    if choice == "save":
        save(people)
    elif choice == "load":
        load()
    elif choice == "yes":
        print("Whose ID number do you want to update?")
        for index, person in enumerate(people, 1):
            print(f"{index}. {person.name}")
        
        person_choice = input("Enter your choice (number): ")
        try:
            person_choice = int(person_choice)
        except ValueError:
           print("Invalid input. Please enter a number.")
           time.sleep(2)
           continue

        if 1 <= person_choice <= len(people):
           new_idnum = input("Enter the new ID number: ")
           people[person_choice - 1].set_idnum(new_idnum)
           print(f"Updated {people[person_choice - 1].name}'s ID number.")
           print(people[person_choice-1])

        else:
            print("Invalid input. Please select a valid person number.")
            time.sleep(2)
    elif choice == "no":
        print("No IDs updated.")
        break
    else:
        print("Invalid choice. Please choose 'yes', 'no', 'save' or 'load'.")
        time.sleep(2)
