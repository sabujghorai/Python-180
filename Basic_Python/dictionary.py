dict = {
  "name" : "sanbuj ghorai ",
  "age" : 21,
  "learning" : "python",
  "subjects" : ["chemistry","English","C programming","hermony","Design THinking"], # we can store a list also
  "marks" : (95,91,97,85,87), # we can store tuple also
  "is_adult" : True, # we cal store a boolean value
  "marks" : (987,73,923) # we cannot assign same key value if we use then it will not run..
  
}
print(dict["name"])
print(dict["age"])
print(dict["learning"])

# nested dictionary......
student = {
  "name" : "Sabuj Ghorai",
  "subject" : {  # nested dictionary
    "phy" : 95,
    "chem" : 91,
    "maths" : 93
  }
}
print(student["subject"])
print(student["subject"]["chem"])



# print how many even and odd number in the range of 1 to N .
n=int(input("enter the range: "))
e_count=0
o_count=0
for i in range (1,n+1):
    if i%2==0:
        e_count+=1
    else :
        o_count+=1

print(e_count)
print(o_count)