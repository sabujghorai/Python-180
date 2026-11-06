#traffic light signals using if,elif,else
light = input("Enter the colour of the light in small letter :")
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look") # the 4 spaces are called indentation
else:
    print("please enter a valid colour..")
