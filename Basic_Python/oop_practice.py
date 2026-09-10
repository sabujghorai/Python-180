# Define a Circle class to create a circle  without radius using the constructor
# Define Area() method and Perimeter() method 

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return 3.14*self.radius**2
    
    def Perimeter(self):
        return 2*3.14*self.radius


a = int(input("Enter the radius :"))
c2 = Circle(a)
print(c2.Area())
print(c2.Perimeter())

# Define a Employee class with attribute role,department & salary.
# the class also have a showDetail() method
class Employee:
    def __init__(self, role, dpt, salary):
        self.role = role
        self.dpt = dpt
        self.salary = salary

    def showDetail(self):
        print("Role =", self.role)
        print("Department =", self.dpt)
        print("Salary =", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)

engg1 = Engineer("Elon Musk", 45)
engg1.showDetail()

class Student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"Branch : {self.branch}")


Student1 = Student("Sabuj",21,"CSE")
Student1.display()


class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand :{self.brand}")
        print(f"Model :{self.model}")
        print(f"Price :{self.price}")

car1 = Car("BMW","M4","1.9cr")
car1.display()