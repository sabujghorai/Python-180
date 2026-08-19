  # FOR LOOPS
# for loop in list

list = ["hello","world","sabuj","ghorai"]
for i in list:
   print(i)
else:
   print("END")

# we can use for loop in string also
   num = ( 1,4,63,35)
   for i in num:
      print(i)
# we can use for loop in string as well

name = "hello users how are you ?"
for i in name :
  if i == 'w':
    print("i found")
    break
  print(i)
else:
  print("😊")

for i in range(5): # range(stop) prints 0 to (n-1)=4
  print(i)
print("range 5 ends here")
  
for j in range(1,5): # range(start,stop)
    print(j)
print("range(1,5) ends here")

for k in range(1,6,2): # range(start? , stop, step)
  print(k)
print("range(1,6,2) ends here")

# PASS STATEMENT
# pass is a null statement that does nothing . It is used as a placeholder for future code

for i in range(5):
  # we want to empty
  pass
print("pass statement does nothing")
