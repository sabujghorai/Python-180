# basic syntax for a while loop
# count = 1
# while count <= 10:
#   a = "hello"
#   print(a,count)
#   count += 1

# # printing 1 to 5 in increasing order
# i = 1
# while i<=5:
#   print(i)
#   i +=1

#     # printing 5 to 0 in decreasing order
# j = 5
# while j>=1:
#   print(j)
#   j-=1 # time complexity will be n

# n = 5
# m = 10
# print(m+n)
# for i in range(0,n):
#     for j in range(0,m,2):
#         print("hello") # time complexity will be (n^2)

# n = 10
# while(n >=1):
#     print("hello")
#     n = n//2 # time complexity will be log(n)

l = [10,2,3,40,5]
for i in range(0,len(l)):
    print(l[i],end=" ")
