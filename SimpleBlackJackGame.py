#Made by Jace Kim 9/19/18
#Modified by 

#Need account to play (You can change the username and password by replacing)----|
#					v------------------------------------------------------------|
import sys
username = input("Username: ")
password = input("Password: ")
if username == "Username":
	if password == '':
		print("Password")
	else: 
		print("YOU ARE BANNED FROM THIS CASINO")
		sys.exit() #If the password is wrong the program will end,
		# but if you get it correct u should be able to play the game

