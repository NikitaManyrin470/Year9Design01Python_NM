import os 



#we use the input function to take an input
#we have to have an assignment statement to store an input

#input is a function. it runs a small program that
#causes the computer to stop and wait for input

#fu

fName = input ("what is your first name: ")
print("Hi, "+fName)

lName = input("What is your last name: ")

print("Hi,"+fName+" "+lName)

initialName = fName[0] + "." +lName 	#adding strings is concatinatio, which is a fancy word for adding strings

print("Hi, "+initialName)
os.system("say " +fName+" "+lName)
