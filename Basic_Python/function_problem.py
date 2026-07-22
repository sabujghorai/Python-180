# average of 3 numbers
def average(a,b,c):
  avg = (a+b+c)/3
  print(avg)
  return sum

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
average(a,b,c)

# default parameter
def sum(a=5,b=7):
  avg = (a+b)/2
  print(avg)
  return avg

sum() # we are not assigning the argument

# sum of two numbers taking input from users
def number(a,b):
  sum = a+b
  print(sum)
  return

a = int(input("Enter a number:"))
b = int(input("Enter another number :"))
number(a,b)

# code for finding fibonacci series

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the term : "))  # Number of terms
print(f"Fibonacci Series up to {n} terms: {fibonacci(n)}")

# WAP  to print the length of a list(list is s parameter)

number = [10,20,30,40,50,60]

def print_length(a):
  print(len(a))

print_length(number) # function call

# WA function to print the element of a list in a single line (list is a parameter)

element = ["sabuj","ghorai","akash","ghorai"]

def one(a):
  for item in a:
    print(item,end = " ")

one(element)

# write a function of finding factorial of a number getting user input

b = int(input("Enter a number :"))

def print_fact(a):
  fact = 1
  for i in range(1,a):
    fact = fact*i
  print("factorial of your given number is :",fact)

print_fact(b)


# write a program to convert USD to INR

b = int(input("Enter your USD value :"))

def inr_value(USD):
  print(b ,"USD =",USD*89.5,"INR")
  return USD*89.5

inr_value(b)