'''
cat subclass of the pet class
'''
import pet  #import the pet superclass

class cat(pet.Pet): # a class based on the superclass "pet"
    
    def __init__(self, pname,ptype,page):  #construct an object but use local copies of the attributes
        super().__init__(pname,ptype,page)
    
    def make_noise(self):                 #overide the super.make_noise
        return("meeeeeeeeeeeoooooowwwww")


def start_demo():
    pet1 = cat("henry","cat","10")

    print(pet1.describe_pet())
    print(pet1.make_noise())
               
if __name__ == "__main__":
    start_demo()
