
class Pet:

    def __init__(self,pname,ptype,page):
        self.pname = pname
        self.ptype = ptype
        self.page = page

    def describe_pet(self):
        return(str(self.pname + " is a " +self.ptype+ " and is "+self.page+" years old"))

    def make_noise(self):
        return(str(self.pname+" makes a "+self.ptype+" noise"))


def start_demo():
    pet1 = Pet("sally","dog","12")
    pet2 = Pet("henry","cat","10")

    print(pet1.describe_pet())
    print(pet1.make_noise())
    
    print(pet2.describe_pet())
    print(pet2.make_noise())
               
if __name__ == "__main__":
    start_demo()
