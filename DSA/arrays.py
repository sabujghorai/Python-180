from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)

for i in range(0,len(val)): # better syntax
    print(val[i],end=" ")

print("\n")
for x in val: # enhance for loop to print the array
    print(x,end=" , ")


from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)

print("\n")
print(val.typecode) # prints i ---> typecode is integer

val.reverse() # reverse the array
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")


from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)


val.insert(0,50) # 0 is the index and 50 is the new adding element
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")

from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)


val.append(50) # at the element at the end
val[2] = 100 # replace the second element with 100
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")

# make a copy of the old array and print the value 
from array import *
val = array('i',[1,2,3,4,5,6])
new_array = array(val.typecode,(x for x in val))
# new_array = array(val.typecode,(x*2 for x in val))

# new_array.pop(3) # to remove the el of index 3
new_array.remove(4) # to remove the element directly


for i in range (0,len(new_array)):
    print(new_array[i],end=" ")
print("\n")

from array import *
a = array('i',[1,2,3,4,5,6,7,8,9,10])
slicing = a[1:7] # idx 7 will not print

for i in range(0,len(slicing)):
    print(slicing[i],end=" , ")

print("\n")

from array import *
a = array('i',[1,2,3,4,5,6,7,8,9,10])
slicing = a[1:-2] # if we don't want the last 2 elements

for i in range(0,len(slicing)):
    print(slicing[i],end=" , ")

print("\n")


from array import *
a = array('i',[1,2,3,4,5,6,7,8,9,10])
slicing = a[::-1] # no starting idx and not ending idx 

for i in range(0,len(slicing)):
    print(slicing[i],end=" , ")

print("\n")

from array import *
a = array('i',[1,2,3,4,5,6,7,8,9,10])
slicing = a[1:7:2] # 2 step jumps

for i in range(0,len(slicing)):
    print(slicing[i],end=" , ")
print("\n")