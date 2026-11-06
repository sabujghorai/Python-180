hello = [12,16,19,23,21,18,17]
hello.append(5) #add one element at the end 
print(hello)
hello.sort() # sort in ascending order
print(hello)
hello.sort(reverse=True)# sort in descending order
print(hello)
hello.reverse() # reverse the list values
print(hello)
hello.insert(5,15)
print(hello)

# let's understand this with charachter 

list = ['apple','cat','banana','duck','kolkata','zoo','prize','super']
list.append('gopal') 
print(list)# add 'gopal' at the end
list.sort()
print(list) # sort the value in the alphabetic order
list.reverse()
print(list) # reverse the list value
list.sort(reverse = True)
print(list) # sort the value in decending order