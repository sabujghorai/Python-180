# del keyword
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("sabuj")
print(s1.name) # first it will print the name sabuj
del s1.name # output will be an error because name attribute is already deleted
print(s1.name)# error

# Private(like) attribute & method
class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num = acc_num # public attribute
        self.__acc_pass = acc_pass # private attribute 

    def reset_pass(self):
        print(self.__acc_pass)

a = Account("123456","pass@1234")
print(a.acc_num)
print(a.reset_pass()) # now it will orint the password
print(a.__acc_pass)# print error 'Account' object has no attribute 'acc_pass'
class Person:
    __name = "hello" # private class attribute

    def __hello(self): # creating a private object
        print("hello users")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
# print(p1.__name)# it will also show an erroor because the __name ia a private attribute

# Inheritence
class Car:
    colour = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): # the Toytacar is the subcatagory of the Car
    def __init__(self,name):
        self.name = name

c = ToyotaCar("toyota corola")
print(c.name)
print(c.colour)
print(c.start())

# Question
#create an ElectricCar class that inherits the car class and has an additional attribute battery_size
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class ElectricCar(Car): # The Car inheritence added
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)
# these are the single lever inheritence

# multi level inheritence
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __ini__(self,name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Electric car..")
car1.start()
print(car1.type)

# Multiple inheritence
class A:  #parent class 1
    var1 = "good morning 1"

class B: # parent class 2
    var2 = "good morning 2"

class C(A,B):
    var3 = "gppd morning 3"

c1 = C()
print(c1.var1)
print(c1.var2)
print(c1.var3)

# Super() method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

c = ToyotaCar("Prius", "Electric car")
print(c.name)
print(c.type)

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

# # polymorphism
# the addition of complex numbers
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,number2): # we are using the dunder function
        newReal = self.real + number2.real
        newImg = self.img + number2.img
        return Complex(newReal,newImg)
        
    def __sub__(self,number2): # here we are using the dunder substraction function
        newReal = self.real - number2.real
        newImg = self.img - number2.img
        return Complex(newReal,newImg)

    def __mul__(self,number2): # here we are using the dunder multiplication function
        newReal = self.real * number2.real
        newImg = self.img * number2.img
        return Complex(newReal,newImg)
        
    def __truediv__(self,number2): # here we are using the dunder multiplication function
        newReal = self.real * number2.real
        newImg = self.img * number2.img
        return Complex(newReal,newImg)
    

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(3,5)
num2.showNumber()

print("---------")
num3 = num1 + num2# if we write this without using the dunder function it will show an error
num3 = num1 - num2
num3 = num1 * num2
num3 = num1 / num2
# num3 = num1.add(num2)
num3.showNumber()
