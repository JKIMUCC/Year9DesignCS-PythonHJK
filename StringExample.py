#This file will go through the basics of
#String Manipulation

#Strings are collections of characters
#String are enclosed in " " or ' '
# "Paul"
# "Paul is cool"
# "Paul is cool!"

#Two things we need to talk about
#when we think of strings
#index - Always starts at 0
#Length

#Example
# 0123		012345
# "Paul"		"Monkey"
# len("Paul") = 4
# len("Monkey") = 6

name = "Jace"

print(name) #I can print strings

sentence = name + " is cool"
print(sentence)
print(sentence + "!")

#I can access specific letters
fLetter = name[0] #name at 0
print(fLetter)
letters1 = name[0:2] # inclusive:exclusive
print(letters1)
letters2 = name[2:]
print(letters2)#formal way of writing letters

letter2a = name[2:len(name)]
print(letter2a)

letters3 = name[:2]
print(letters3)

lname = len(name) #length of string
print(lname)

#if I want to print out all letters
for i in range(len(name)):
	print(name[i])