class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def make_sound(self):
      return "Generic animal sound"


class Cat(Animal):
    def __init__(self, name, age, breed = "Domestic Short Hair"):
      super().__init__(name, age)
      self.breed = breed
    def make_sound(self):
        return "Meow!"

    def purr(self):
        return "Purrrrr..."

    def scratch(self):
        return "Scritch! Scratch!"
    
    def get_breed(self):
      return self.breed

class Dog(Animal):
    def __init__(self, name, age, breed ="Mixed"):
      super().__init__(name, age)
      self.breed = breed

    def make_sound(self):
        return "Woof!"

    def bark(self):
        return "BARK! BARK!"

    def fetch(self):
        return "The dog fetches the ball!"

    def get_breed(self):
      return self.breed

class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "The bird soars through the sky."

    def sing(self):
        return "Tweet tweet!"

    def get_species(self):
       return self.species

class Fish(Animal):
    def __init__(self, name, age, habitat):
      super().__init__(name,age)
      self.habitat = habitat

    def make_sound(self):
        return "Blub!"

    def swim(self):
      return "The fish glides through the water"

    def get_habitat(self):
       return self.habitat

# Example Usage
if __name__ == "__main__":
    cat = Cat("Whiskers", 3, "Siamese")
    dog = Dog("Buddy", 5, "Golden Retriever")
    bird = Bird("Tweety", 1, "Canary")
    fish = Fish("Nemo", 2, "Ocean")

    print(f"{cat.get_name()} says: {cat.make_sound()}")
    print(f"{cat.get_name()} is {cat.get_age()} years old and a {cat.get_breed()}")
    print(f"{cat.get_name()} is {cat.purr()}")
    print(f"{cat.get_name()} is {cat.scratch()}")
    print()

    print(f"{dog.get_name()} says: {dog.make_sound()}")
    print(f"{dog.get_name()} is {dog.get_age()} years old and a {dog.get_breed()}")
    print(f"{dog.get_name()} is {dog.bark()}")
    print(f"{dog.get_name()} is {dog.fetch()}")
    print()
    
    print(f"{bird.get_name()} says: {bird.make_sound()}")
    print(f"{bird.get_name()} is {bird.get_age()} years old and a {bird.get_species()}")
    print(f"{bird.get_name()} is {bird.fly()}")
    print(f"{bird.get_name()} is {bird.sing()}")
    print()

    print(f"{fish.get_name()} says: {fish.make_sound()}")
    print(f"{fish.get_name()} is {fish.get_age()} years old and from the {fish.get_habitat()}")
    print(f"{fish.get_name()} is {fish.swim()}")
