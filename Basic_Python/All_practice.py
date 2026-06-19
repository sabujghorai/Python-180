# Print a multiplication table for a number.

a = int(input("Enter the number for multiplication table :"))

for i in range(1,11):
    print(a,"x", i, "=" ,a*i)


# Check if a number is prime.

number = (int(input("Enter the number to check the number is prime or not :")))

if number <= 1 :
    print("Not prime")

else:
    is_prime = True
    for i in range(2 , number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Prime")
    else:
        print("not prime")


# Find the factorial of a number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

fact = int(input("Enter the number for factorial :"))
print("Factorial is : " , factorial(fact))

#  Make a simple calculator 