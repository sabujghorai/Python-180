class Car: # first letter must be capital letter 'c'ar
    car_name = "Mercedese Benz"
    model_no = 23
    colour = "Blue"

s1 = Car() # creating aa object
print(s1.car_name)
print(s1.model_no)
print(s1.colour)


# __init__ function --> also call constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("mercedese","Benz")
print(my_car.brand)
print(my_car.model)
# making a new brand and model
my_new_car = Car("TATA","safari")
print(my_new_car.brand)
print(my_new_car.model)

# basic class and object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Object creation
s1 = Student("Sabuj", 21)
s1.display()

# Rectangle area (Method example)
class Rectangle:
    def set_values(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle()
r.set_values(5, 3)
print("Area:", r.area())


class Student:
    collage_name = "Brainware Univercity"
    name = "Mr."
    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("from :",Student.collage_name)


c1 = Student("karan","unknown")
print(c1.name) # print name karan first 
# because object preference > the class preference


# opp class with methods methods 
class Student:
    collage_name = "Brainware University"
    location = "Berasat"
    
    def __init__(self,fullname):
        self.fullname = fullname
        
    def hello(self): # method name is hello
        print(self.fullname)
        
s = Student("hello sabuj ghorai") #object name is 's'
s.hello() # to use method use write object name dot method name

# Question
# create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi",self.name,"your avg score is",sum/3)

s = Student("Krishna", [95,97,99])
print(s.name,s.marks)
s.average()

# static method --> work at class level
class Student:
    def __init__(self,name):
        self.name = name

    @staticmethod # decorator
    def hello():
        print("hello")

s = Student("karan")
s.hello()
print(s.name)

# Abstruction --> hiding the unnecessary
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True #unnecessary
        self.acc = True #unnecessary
        print("car started...")

car1 = Car()
car1.start()

# question 
#  create Account class with two attributes balance & account no
# now create a method for debit,credit and printing the balance
class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account_no = account

    #debit method
    def debit(self,ammount):
        self.balance -= ammount
        print("RS.",ammount,"was debited")
        print("total balance = ",self.get_balance())

    def credit(self,ammount):
        self.balance += ammount
        print("RS.",ammount,"was credited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000,95859384242)
acc1.debit(1000)
acc1.credit(5000)

# class method
class Person:
    name = "sabuj Ghorai"

    # def changeName(self,new_name):
    #     self.new_name = new_name

# insted of doing this we can use the callmethod
    @classmethod  # decorator
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Akash Ghorai")
print(p1.name) # also works
print(Person.name) # correct way

#property
class Student:

    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = ((self.phy+self.chem+self.math)/3),"%"

    # def calPercentage(self):
    #     self.percentage = ((self.phy+self.chem+self.math)/3),"%"
    
# insted of doing this we can use the @property method

    @property
    def percentage(self): # the method name is percentage
        return ((self.phy+self.chem+self.math)/3),"%"
    

a = int(input("Enter the marks of physics :"))
b = int(input("Enter the marks of chemistry :"))
c = int(input("Enter the marks of maths :"))

s1 = Student(a,b,c)
print(s1.percentage)