# print numbers in reverse order
b = int(input("Enter a number :"))

def show(n):
  if(n == 0): # base case
    return
  print(n)
  show(n-1) # function call

show(b)

# print the factorial of a number using recursion taking from user input

b = int(input("Enter a number :"))

def fact(a):
  if(a == 0):
    return 1
  return a*fact(a-1)

print("factorial of your given number is :",fact(b))

# print the sum of all n natural numbers

n = int(input("Enter a number :"))

def sum(n):
    if (n == 0 ):
        return 0
    return n+sum(n-1)

print("The sum of your ",n,"th term is ",sum(n))
print("sum of your all natural number is :",sum(b))

# fibonacci series of n term taking input from user
n = int(input("Enter the term :"))

def fibo(n):
    if (n == 0):
        return 0
    if(n == 1):
        return 1
    return fibo(n-1)+fibo(n-2)

for i in range(n):
    print(fibo(i),end= " ")
print("These are the fibonacci series...")

# power of a number...
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter base: "))
b = int(input("Enter power: "))
print("Result:", power(a, b))

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))

# count digit in a numbere
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))

# write a recursive function to print all element in a list 
# Hint : use & index as parameter

def print_list(list,idx=0):
   if (len(list) == idx):
      return
   print(list[idx])
   print_list(list,idx+1)
fruit = ["mango","banana","lichi","orange"]
print_list