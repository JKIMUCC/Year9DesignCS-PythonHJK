import tkinter as tk
from tkinter import *
import math






class paceCalculator:

	#**def clear_search(event):
		#self.entTime.delete(0, END)
	#***def clear_search2(event):
		#self.entDS.delete(0, END)

	def __init__(self):
		self.root = tk.Tk()
		self.root.configure(background = "navy")
		self.root.geometry('400x400')

		self.labTitle = tk.Label(self.root,text = "Pace Calculator")
		self.labTitle.grid(row = 2, column = 0, columnspan = 2)

		self.labTime = tk.Label(self.root, text = "Enter Time in Seconds: ")
		self.labTime.grid(row = 3, column = 0)
		self.entTime = tk.Entry(self.root, background = "light grey")
		self.entTime.grid(row = 3, column = 1)
		#self.entTime.insert(0,"Enter Time in Seconds")
		#self.entTime.bind("<Button-1>", clear_search)

		self.labDS = tk.Label(self.root, text = "Enter Distance Swam: ")
		self.labDS.grid(row = 4, column = 0, padx = 10, pady = 10)
		self.entDS = tk.Entry(self.root, background = "light grey")
		self.entDS.grid(row = 4, column = 1, padx = 10, pady = 10)
		#**self.entDS.insert(0,"Enter Distance in Meters")
		#***self.entDS.bind("<Button-1>", clear_search2) 

		self.DDLabel = Label(self.root, text = "Select Distance: ")
		self.DDLabel.grid(row = 5 , column = 0, sticky = "E")

		OPTIONS = [ 
		"25",
		"50",
		"100",
		"200",
		]
		self.var = tk.StringVar(self.root)
		self.var.set(OPTIONS[0])

		self.dropDownMenu = tk.OptionMenu(self.root,self.var, OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3])
		self.dropDownMenu.grid(row = 5 , column = 1, sticky = "W")
d
		self.btnCalc = tk.Button(self.root, text = "Calculate",command= self.calculate)
		self.btnCalc.grid(row = 6 , column = 0, columnspan = 2)
		self.output = tk.Text(self.root, height = 10, width=50, relief=tk.GROOVE)
		self.output.config(state="disabled")
		self.output.grid(row = 8, column = 0, columnspan = 2)

		self.root.mainloop()


	def calculate(self):
		print("Calculating")

		t = float(self.entTime.get())
		d = float(self.entDS.get())
		c = float(self.var.get())

		r = math.ceil((t/d)*c)


		outputValue = "When "+str(t)+" seconds is taken to swim "+str(d)+" meters,   the pace per "+str(c)+"meters is:" + str(r) + " seconds per " + str(c)


		self.output.config(state = "normal")

		self.output.delete(1.0,tk.END)
		self.output.insert(tk.INSERT,outputValue)
		self.output.config(state="disabled")
		print(str(r) + "Seconds per" + str(c))

paceCalculator()

