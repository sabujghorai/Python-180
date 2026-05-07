# del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("sabuj")
print(s1.name)

del s1.name

# checking before printing
if hasattr(s1, "name"):
    print(s1.name)
else:
    print("name attribute deleted")


# Private(like) attribute & method
class Account:
    def __init__(self, acc_num, acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

a = Account("123456", "pass@1234")

print(a.acc_num)
a.reset_pass()

# print(a.__acc_pass)  # ERROR


class Person:
    __name = "hello"

    def __hello(self):
        print("hello users")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()

# print(p1.__name) # ERROR


# Inheritance
class Car:
    colour = "black"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


c = ToyotaCar("toyota corolla")

print(c.name)
print(c.colour)
c.start()


# Electric Car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85KWh")

print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)


# Multilevel inheritance
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):

    def __init__(self, name):   # corrected __init__
        self.name = name


class Fortuner(ToyotaCar):

    def __init__(self, type):
        self.type = type


car1 = Fortuner("Electric car")

car1.start()
print(car1.type)


# Multiple inheritance
class A:
    var1 = "good morning 1"


class B:
    var2 = "good morning 2"


class C(A, B):
    var3 = "good morning 3"


c1 = C()

print(c1.var1)
print(c1.var2)
print(c1.var3)


# super() method
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


# classmethod
class Person:
    name = "sabuj Ghorai"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("Akash Ghorai")

print(p1.name)
print(Person.name)


# property decorator
class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return f"{(self.phy + self.chem + self.math) / 3}%"


a = int(input("Enter marks of physics: "))
b = int(input("Enter marks of chemistry: "))
c = int(input("Enter marks of maths: "))

s1 = Student(a, b, c)

print(s1.percentage)


# Polymorphism
class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} + {self.img}i")

    def __add__(self, number2):
        newReal = self.real + number2.real
        newImg = self.img + number2.img
        return Complex(newReal, newImg)

    def __sub__(self, number2):
        newReal = self.real - number2.real
        newImg = self.img - number2.img
        return Complex(newReal, newImg)

    def __mul__(self, number2):
        newReal = (self.real * number2.real) - (self.img * number2.img)
        newImg = (self.real * number2.img) + (self.img * number2.real)
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num2 = Complex(3, 5)

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

num5 = num1 * num2
num5.showNumber()


# Basic class and object
class Car:

    car_name = "Mercedes Benz"
    model_no = 23
    colour = "Blue"


s1 = Car()

print(s1.car_name)
print(s1.model_no)
print(s1.colour)


# constructor example
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Mercedes", "Benz")

print(my_car.brand)
print(my_car.model)

my_new_car = Car("TATA", "Safari")

print(my_new_car.brand)
print(my_new_car.model)


# Student class
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Sabuj", 21)
s1.display()


# Rectangle area
class Rectangle:

    def set_values(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle()

r.set_values(5, 3)

print("Area:", r.area())


# Student average question
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        print("Hi", self.name, "your average score is", total / len(self.marks))


s = Student("Krishna", [95, 97, 99])

print(s.name, s.marks)

s.average()


# static method
class Student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello():
        print("hello")


s = Student("karan")

s.hello()

print(s.name)


# Abstraction
class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")


car1 = Car()

car1.start()


# Bank account question
class Account:

    def __init__(self, balance, account):
        self.balance = balance
        self.account_no = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 95859384242)

acc1.debit(1000)

acc1.credit(5000)