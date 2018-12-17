#This imports the tkinter "tool box" this contains. 
#All the support material to make GUI elements.
#By including "as tk" we are giving a short name to use. 
import tkinter as tk 


# Main Window
root = tk.Tk()	#creates standard main window


#Three stages to build all elements/obkects.
#1. Construct the object: We build and configure it. 
#2. Configure the object: We specify behaviours and settings.
#3. Pack the object: Putting it into the window. 
output = tk.Text(root,height = 10, width = 30)
 #Parameters are what we send. 
#ordered paramters: The order where we send them in matters. (common)
#named parameters: JavaScript and Python specific. 
output.config(background = "grey")
output.grid(row = 0, column = 0, rowspan = 5)

#****** Labels ********

labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0)

#****** Checkboxes ********
#How do I track the checkmark state?
var1 = tk.IntVar()
var2 = tk.IntVar()
#What the named parameter variable does is binds the IntVar to the checkbox.
#If there is a change in the box, there is a change in the cariable. 
#This is called binding.

cHC= tk.Checkbutton(root, text="Expand", variable = var1)
cHC.grid(row = 0, column = 1)

cLF = tk.Checkbutton(root, text="Expand", variable= var2)
cLF.grid(row = 1,  column = 1)


#We are writing an EVENT DRIVEN PROGRAM.
#Build the GUI.
#Start it running.
#Wait for "EVENT".

root.mainloop() #starts the program
