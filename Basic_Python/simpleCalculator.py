print("Calculator")

print("Enter 1 for addition")
print("Enter 2 for difference")
print("Enter 3 for product")
print("Enter 4 for division")

choice = int(input("Enter the choice : "))

b = int(input("Enter first number : "))
c = int(input("Enter second number : "))

if choice == 1:
    print("Sum is :", b + c)

elif choice == 2:
    print("Difference is :", b - c)

elif choice == 3:
    print("Product is :", b * c)

elif choice == 4:
    if c != 0:
        print("Division is :", b / c)
    else:
        print("Error: Division by zero")

else:
    print("You have entered a wrong choice")