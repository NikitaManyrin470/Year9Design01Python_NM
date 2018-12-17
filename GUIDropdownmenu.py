import tkinter as tk

def change(event):
	print("running change")
	print(var.get())

root = tk.Tk() #Constructs the main window.

#List of strings.
#My list is called optiones. There are 3 elements with index 0-2. 
#print(OPTIONS[2])
OPTIONS = [

	"eggs",
	"bunny",
	"chicken", 

]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS [0], OPTIONS [1], OPTIONS [2])
dropDownMenu.pack()
root. mainloop()
print("End program")