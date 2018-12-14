import tkinter as tk
from tkinter import *




root = tk.Tk()
root.configure(background = "navy")
root.geometry('400x400')

def clear_search(event):
   entTime.delete(0, END) 
def clear_search2(event):
   entDS.delete(0, END) 

class paceCalculator:
    def __init__(self):
        window = Tk()
        window.title("Pace Calculator")

        def result(z1,z2,z3):
            biz=(z1/z2)*z3
            lblresult.delete(0,END)
            lblresult.insert(0,biz)
            return

        labTitle = tk.Label(root,text = "Pace Calculator")
        labTitle.grid(row = 2, column = 0, columnspan = 2)
        labTime = tk.Label(root, text = "Enter Time: ")
        labTime.grid(row = 3, column = 0)

        self.num1Var = IntVar()
        entTime = tk.Entry(root, background = "light grey", self.num1Var, justify = RIGHT)
        entTime.grid(row = 3, column = 1)
        entTime.insert(0,"Enter Time in Seconds")
        entTime.bind("<Button-1>", clear_search)
        labDS = tk.Label(root, text = "Enter Distance Swam: ")
        labDS.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.num2Var = IntVar()
        entDS = tk.Entry(root, background = "light grey", self.num2Var, justify = RIGHT)
        entDS.grid(row = 4, column = 1, padx = 10, pady = 10)
        entDS.insert(0,"Enter Distance in Meters")
        entDS.bind("<Button-1>", clear_search2) 

        DDLabel = Label(text = "Select Distance: ")
        DDLabel.grid(row = 5 , column = 0, sticky = "E")

        OPTIONS = [ 
        "25",
        "50",
        "100",
        "200",
        ]

        var = tk.StringVar(root)
        var.set(OPTIONS[0])

        self.num3Var = IntVar()
        dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3], self.num3Var, justify = RIGHT)
        dropDownMenu.grid(row = 5 , column = 1, sticky = "W")

        btnCalc = tk.Button(root, text = "Calculate", command ,command=lambda:result(self.num1Var.get(),self.num2Var.get(), self.num3Var.get())
        btnCalc.grid(row = 6 , column = 0, columnspan = 2)

        output = tk.Entry(root, background = "light grey", height = 10, width = 50, font = ("Arial",12))
        output.config(state = "disable")
        output.grid(row = 7 ,column = 0, columnspan = 2)














		root.mainloop()

paceCalculator()

