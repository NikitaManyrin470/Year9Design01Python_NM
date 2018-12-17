import tkinter as tk
import math

def submit():

	print("Submit Pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state = "normal")
	output.insert(tk.INSERT,v)
	output.config(state = "disabled")

root = tk.Tk()
root.title("Volume of A Cylinder")

labr= tk.Label(root,text="radius")
labr.grid(column = 0, row = 0)

entr = tk.Entry(root)
entr.grid(column = 0, row = 1)

labh = tk.Label(root, text = "height")
labh.grid(column = 0, row = 2)

enth = tk.Entry(root)
enth.grid(column = 0, row = 3)

btn = tk.Button(root, text = "Submit", command = submit)
btn.grid(column = 0, row = 4)

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief=tk.GROOVE)
output.config(state = "disabled")
output.grid(column = 0, row =5)



root.mainloop()

