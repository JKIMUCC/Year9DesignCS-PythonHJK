import sys
import tkinter as tk


root = tk.Tk()
labUN = tk.Label(root, text = "Username")

labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx = 10, pady = 10)

labPass = tk.Label(root, text = "Password")
labPass.pack()

entPass = tk.Entry(root, show = "*")
entPass.pack(padx = 10, pady = 10)



def login():
	if entUN == "Username":
		if entPass == 'Password':
			output.print("Password accepted")
			os.system("python3 PaceCalculatorPage.py")
			sys.exit()
		else: 
			output.print("Wrong Username or Password")
			


btnLogin = tk.Button(root, text = "Login", command= login)
btnLogin.pack()



output = tk.Text(root, background = "light grey", height = 10, width = 50, font = ("Arial",12))
output.config(state = "disable")
output.pack()












root.mainloop()