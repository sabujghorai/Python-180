# nested if
age = int(input('Enter the age :'))
if(age>=18):
  if(age>=65):
    print("cannot drive due to old age")
  else:
    print("you can drive")
else:
  print("cann not drive because you are not adult")