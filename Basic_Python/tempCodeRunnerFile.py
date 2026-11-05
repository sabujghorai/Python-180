b = int(input("Enter a number :"))

def print_fact(a):
  fact = 1
  for i in range(1,a+1):
    fact = (fact*i)
  print("factorial of your given number is :",fact)

print_fact(b)