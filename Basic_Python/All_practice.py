# Print a multiplication table for a number.

# a = int(input("Enter the number for multiplication table :"))

# for i in range(1,11):
#     print(a,"x", i, "=" ,a*i)


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