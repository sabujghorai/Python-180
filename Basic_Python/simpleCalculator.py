print("Calculator")

print("Enter 1 for addition")
print("Enter 2 for difference")
print("Enter 3 for product")
print("Enter 4 for division")

b = int(input("Enter a number :"))
c = int(input("Enter another number :"))


choice = int(input("Enter the choice :"))
if choice == 1:
    print("sum is :",b+c)

elif choice == 2:
    print("Difference is :",b-c)

elif choice ==3:
    print("product is :",b*c)

elif choice == 4:
    if c != 0:
        print("Difference is :",b/c)
    else:
        print("error division by Zero")

else:
    print("You have entered a wrong choice..")
