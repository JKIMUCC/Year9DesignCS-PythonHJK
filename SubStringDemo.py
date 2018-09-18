#This program will show how to effectivly use substring
#Prompt the User for their first name and their last name

#Input
fName = input("What is your first name: ")
lName = input("What is your last name: ")

username = input("Username: ")
password = input("Password: ")
#Process
result = fName[0] + "." + lName
#Create a code name by using letters of their first and last name
codename = fName[3] + fName[2] + fName[1] + fName[0]
#Output
print("Hi "+result)
print("Codename is: "+codename)
