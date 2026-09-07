import math

# WAP to calculate the LCM of two numbers
A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
C = int(input("Enter third number : "))
D = int(input("Enter foourth number : "))
E = int(input("Enter fifth number : "))
F = int(input("Enter sixth number : "))

result = math.lcm(A,B,C,D,E,F)
print("LCM is :",result)


# WAP to calculate the distance between two coordinates 
x1 = float(input("X1 :"))
x2 = float(input("X2 :"))
y1 = float(input("Y1 :"))
y2 = float(input("Y2 :"))
Distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print(f"Distance is : {Distance}")


# WAP to calculate the roots of the equation
a = int(input("Enter A :"))
b = int(input("Enter B :"))
c = int(input("Enter C :"))

equation1 = (-b + math.sqrt(math.pow(b,2)- 4*a*c)) / (2*a)
equation2 = (-b - math.sqrt(math.pow(b,2)- 4*a*c)) / (2*a)
print(equation1,equation2)


# WAP to determina the number is perfect sqere root or not
A = int(input("Enter a number :"))
root = math.sqrt(A)
if root*root == A:
    print("Perfect sqere..")
else:
    print("Not perfect Sqere..")