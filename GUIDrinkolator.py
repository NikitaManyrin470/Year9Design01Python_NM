import tkinter as tk
import math

def submit(*args):
	print("Submit pressed")
	global ent1
	global ent2
	global ent3
	global ent4

	ent1 = float(ent1.get())
	ent2 = float(ent2.get())

	ent3 = float(ent3.get())
	ent4 = float(ent4.get())

	output = math.ent1-ent2/ent1*100

	output.config(state = "normal")
	output.insert(tk.INSERT,v)
	output.config(state = "disabled")

def submit1(*args):
	print("Submit Pressed")
	

root = tk.Tk()
root.title("The Drinkolator")


labInput1 = tk.Label(root,text = "Welcome to the Drinkolator!")
labInput1.grid(column = 0, row = 0, columnspan = 3)

labInput2 = tk.Label(root,text="Drink Price A")
labInput2.grid(column = 0, row =1 )

labInput3 = tk.Label(root,text="Drink Price B")
labInput3.grid(column = 0, row = 3)

labInput4 = tk.Label(root, text="Drink Volume A")
labInput4.grid(column = 1, row =1 )

labInput5 = tk.Label(root, text = "Drink Volume B")
labInput5.grid(column = 1, row =3 )

labInput6 = tk.Label(root, text = "Quantity",borderwidth = 2, relief = "solid")
labInput6.grid(column =5, row = 1)

labInput7 = tk.Label(root, text = "Sugar",borderwidth = 2, relief = "solid")
labInput7.grid(column = 6, row = 1)

labInput8 = tk.Label(root, text = "Calories", borderwidth = 2, relief = "solid")
labInput8.grid(column = 7, row = 1)

labInput9 = tk.Label(root, text = "Milliliters",borderwidth = 2, relief = "solid")
labInput9.grid(column = 8, row = 1)

labInput10 = tk.Label(root, text = "Total", borderwidth = 2, relief = "solid")
labInput10.grid(column = 9, row = 1)

ent1 = tk.Text(root, width = 10, height = 1.25, relief = "solid")
ent1.config(relief = "solid", background = "light blue")
ent1.grid(column = 0, row =2 )

ent2 = tk.Text(root, width = 10, height = 1.25, relief = "solid")
ent2.config(relief = "solid", background = "light blue")
ent2.grid(column = 0, row =4 )

ent3 = tk.Text(root, width = 10, height = 1.25, relief = "solid")
ent3.config(relief = "solid", background = "light blue")
ent3.grid(column = 1, row =2 )

ent4 = tk.Text(root, width = 10, height = 1.25, relief = "solid")
ent4.config(relief = "solid", background = "light blue")
ent4.grid(column = 1, row = 4) 

ent5 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent5.config(relief ="groove", background = "light yellow")
ent5.grid(column = 5, row = 2)

ent6 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent6.config(relief ="groove", background = "light yellow")
ent6.grid(column = 6, row = 2)

ent7 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent7.config(relief ="groove", background = "light yellow")
ent7.grid(column = 7, row = 2)

ent8 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent8.config(relief ="groove", background = "light yellow")
ent8.grid(column = 8, row = 2)

ent9 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent9.config(relief ="groove", background = "light yellow")
ent9.grid(column = 5, row = 3)

ent10 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent10.config(relief ="groove", background = "light yellow")
ent10.grid(column = 6, row = 3)

ent11 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent11.config(relief ="groove", background = "light yellow")
ent11.grid(column = 7, row = 3)

ent12 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent12.config(relief ="groove", background = "light yellow")
ent12.grid(column = 8, row = 3)

ent13 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent13.config(relief ="groove", background = "light yellow")
ent13.grid(column = 5, row = 4)

ent14 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent14.config(relief ="groove", background = "light yellow")
ent14.grid(column = 6, row = 4)

ent15 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent15.config(relief ="groove", background = "light yellow")
ent15.grid(column = 7, row = 4)

ent16 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent16.config(relief ="groove", background = "light yellow")
ent16.grid(column = 8, row = 4)

ent17 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent17.config(relief ="groove", background = "light yellow")
ent17.grid(column = 5, row = 5)

ent18 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent18.config(relief ="groove", background = "light yellow")
ent18.grid(column = 6, row = 5)

ent19 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent19.config(relief ="groove", background = "light yellow")
ent19.grid(column = 7, row = 5)

ent20 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent20.config(relief ="groove", background = "light yellow")
ent20.grid(column = 8, row = 5)

ent21 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent21.config(relief = "groove", background = "light yellow")
ent21.grid(column = 9, row =2)

ent22 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent22.config(relief = "groove", background = "light yellow")
ent22.grid(column = 9, row =3)

ent23 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent23.config(relief = "groove", background = "light yellow")
ent23.grid(column = 9, row =4)

ent24 = tk.Text(root, width = 15, height = 1, relief = "groove")
ent24.config(relief = "groove", background = "light yellow")
ent24.grid(column = 9, row =5)


btn = tk.Button(root,text="Submit", command= submit)
btn.grid(column = 0, row = 5, columnspan = 2 )

output = tk.Text(root,width=50,height=10,borderwidth=3,relief=tk.GROOVE)
output.config(state="disabled")
output.grid(column = 0, row = 9, columnspan = 2)



root.mainloop()