import os
# Aloop is a programming structure that can repeat a section of code
#A loop can run the same code exactly over and over or
#with some thought it can generate a pattern

#There are two broad categories of loops
#Conditional Loops (while): These loops as long as a condition is true

#Counted Loop (for): These loop using a counter to keep track of how many 
#					the loop has run
#
#
#You can use any loop in any situation, but usually from a design
#perspective there ie a better loop in terms of coding
#
#
#If you know in advance how many times a loop should run a COUNTED LOOP
#is usually the better choise
#If you don't know how many times a loop should run a CONDITIONAL LOOP
#is usually the better choise

print("******************************************************")
#Taking Inputs


word = ""
#A while loop evaluates a condtion when it is first reached
#If the condition is true it enters the loop block
while (len(word)) <6 or not(word.isalpha()):
	word = input("Please input a word larger than 5 letters: ")

	if(len(word) <6):
		print("YOU! HAD! ONE! job")

if (word.isalpha() == False):
	print("BOI")

	#When we reach the bottom of the loop block we check the condition
	#again. If it is true, we go back to the top of the block and run
	#it again.



print(word+" is a seriously long word")
