student = {
  "name" : "Sabuj Ghorai",
  "subject" : {  # nested dictionary
    "phy" : 95,
    "chem" : 91,
    "maths" : 93
  }
}
print(student.keys()) #prints the key keys ('name') and ('subject')...
print(student.values()) # prints the values phy,chem,math and 95,91,93 respectively...
