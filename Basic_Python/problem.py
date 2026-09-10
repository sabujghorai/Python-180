# this is the code for grading the students according to their marks
mark = int(input("Enter the number from 1 to 100 :"))
if(100>=mark>=90):
  print("grade = A")
elif(90>mark>=80):
  print("grade = B")
elif(80>mark>=70):
  print("grade = C")
elif(70>mark>50):
  print("grade = D")
elif(1<mark<50):
  print("you are failed due to less marks")
else:
  print("you have enter a wrong digit")