import tkinter as tk


root = tk.Tk()
root.configure(background = "blue")






labTitle = tk.Label(root,text = "Pace Calculator")
labTitle.grid(row = 0, column = 0, columnspan = 2)

labTime = tk.Label(root, text = "Enter Time")
labTime.grid(row = 1, column = 0)

entTime = tk.Entry(root)
entTime.grid(row = 1, column = 1)

labDS = tk.Label(root, text = "Enter Distance Swam")
labDS.grid(row = 2, column = 0, padx = 10, pady = 10)

entDS = tk.Entry(root)
entDS.grid(row = 2, column = 1, padx = 10, pady = 10)


btnCalc = tk.Button(root, text = "Calculate")
btnCalc.grid(row = 3 , column = 0, columnspan = 2)



output = tk.Text(root, background = "light grey", height = 10, width = 50, font = ("Arial",12))
output.config(state = "disable")
output.grid(row =4 ,column = 0, columnspan = 2)














root.mainloop()