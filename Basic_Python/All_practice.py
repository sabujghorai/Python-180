# Print a multiplication table for a number.

a = int(input("Enter the number for multiplication table :"))

for i in range(1,11):
    print(a,"x", i, "=" ,a*i)