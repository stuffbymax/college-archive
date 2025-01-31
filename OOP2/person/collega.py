import random

class Person:  
    def __init__(self, pname, ptype, page):
        self.pname = pname
        self.ptype = ptype
        self.page = page
        self.student_id = self.generate_student_id() #calling here, adding student_id to each student
    
    def generate_student_id(self):
         """Generates a random 8-digit student ID."""
         return str(random.randint(10000000, 99999999))
    
    def describe_person(self):  # Fixed typo 'describe_pet' to 'describe_person'
        return str(self.pname + " is a " + self.ptype + " and his ID is " + str(self.page) + " years old"  +" ID: "+self.student_id)
    

def start():
    person1 = Person("Zdislav Wladislav", "Student", 17) 
    person2 = Person("Henry", "Staff", 20)


    print(person1.describe_person())
    
    print(person2.describe_person())
    
start()
