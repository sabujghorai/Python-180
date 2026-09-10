# Write a program that checks if a number is even or odd.
a = int(input("Enter a nimber :"))
if a%2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Take a list of numbers and return their sum
number = [1,3,4,2,5,7,9]
total = sum(number)
print("sum is = ",total)


# Given a list, find the largest number.
list = [20,30,40,50,77,11,85,75,102]
find = max(list)
print("The maximum number is :",find)


# Reverse a String
string = "Hello world"

char_text = ""
for char in string:
    char_text = char+char_text

print("The reversed string is :- ",char_text)

string1 = "good morning"
print("the reversed string is :",string1[::-1])

value = (input("Enter a number or string :"))
for i in range(value):
    for ch in value:
        if value == value[::-1]:
            print("Palindrome")
        else:
            print("Not palindrome")