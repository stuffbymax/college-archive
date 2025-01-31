from datetime import date
 
class Person:
    def __init__(self, name, address, dob):
        self.__name = name
        self.__address = address
        self.__dob = dob
 
    def getName(self):
        return self.__name
 
    def getAddress(self):
        return self.__address
 
    def getDob(self):
        return self.__dob
 
    def displayInfo(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Date of Birth: {self.__dob}")
 
 
class Student(Person):
    def __init__(self, name, address, dob, studentID, major, gpa):
        super().__init__(name, address, dob)
        self.__studentID = studentID
        self.__major = major
        self.__gpa = gpa
 
    def getStudentID(self):
        return self.__studentID
 
    def getMajor(self):
        return self.__major
 
    def getGpa(self):
        return self.__gpa
 
    def displayInfo(self):
        super().displayInfo()
        print(f"Student ID: {self.__studentID}")
        print(f"Major: {self.__major}")
        print(f"GPA: {self.__gpa}")
 
 
class Staff(Person):
    def __init__(self, name, address, dob, staffID, department, jobTitle):
        super().__init__(name, address, dob)
        self.__staffID = staffID
        self.__department = department
        self.__jobTitle = jobTitle
 
    def getStaffID(self):
        return self.__staffID
 
    def getDepartment(self):
        return self.__department
 
    def getJobTitle(self):
      return self.__jobTitle
    def displayInfo(self):
        super().displayInfo()
        print(f"Staff ID: {self.__staffID}")
        print(f"Department: {self.__department}")
        print(f"Job Title: {self.__jobTitle}")
 
 
if __name__ == "__main__":
    person1 = Person("John Doe", "123 Main St", date(1990, 5, 15))
    person1.displayInfo()
    print("-" * 20)
 
    student1 = Student("Alice Smith", "456 Oak Ave", date(2002, 10, 20), 12345, "Computer Science", 3.8)
    student1.displayInfo()
    print("-" * 20)
 
    staff1 = Staff("Bob Johnson", "789 Pine Ln", date(1985, 3, 10), 67890, "IT Department", "Network Admin")
    staff1.displayInfo()
