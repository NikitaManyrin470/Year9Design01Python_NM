import tkinter as tk
import math

print("***Welcome To My Cyldinder Volume Calculator***")

def submit():

	print("Submit pressed")
	r = float(entr .get())
	h = float(enth .get())
	
	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")
	OutputValue = "Given\nradius:"+str(r)+" units\nheight: "+str(h)+" units\nThe Volume Is: "+str(v)+" units cubed\n\n "
	output.delete(1.0,tk.END)

	output.insert(tk.INSERT, OutputValue)
	output.config(state="disable")

root = tk.Tk()
root.title("Volume of Cylinder Calculator")

labr = tk.Label(root,text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root,text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()


btn = tk.Button(root,text="Submit", command=submit)
btn.pack()


output = tk.Text(root,width=50,height=10,borderwidth=3,relief=tk.GROOVE)
output.config(state="disabled")
output.pack()



root.mainloop()

