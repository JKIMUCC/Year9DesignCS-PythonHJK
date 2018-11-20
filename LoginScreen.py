#This imports the tkinter "toolbox" this contains
#all the support material to make GUI elements.

import tkinter as tk
#Pack() is for GUIs with top to bottom elements

root = tk.Tk() #creates the standard main window
#Tk()is a special function called a COSTRUCTER



#Widget 1
#1. Construct the Object
#2. Configure the Object
#3. Pack the Object

labUN = tk.Label(root, text = "Username")
#ordered parameters: The order we send them matters
#named parameters: Javascript and Python Specific
labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx = 10, pady = 10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root, show = "*")
entPassword.pack(padx = 10, pady = 10)



btnLogin = tk.Button(root, text = "Login")
btnLogin.pack()



















root.mainloop()