#loops are structures used to repeat sections of code.
#they are useful if you have to do the same thing more than once.
#or you can establish a pattern
#example 1:

print("******")
#This is a counted loop. We need to thik about count, check, change.
#i = 0, 0 < 5 = TRUE, run loop. 
#i = 1, i < 5, TRUE -run loop
#i = 2, 2 < 5, TRUE- RUN LOOP
#I = 3, 3 < 5, TRUE - RUN LOOP
#I = 4, 4<5, TRUE- RUN LOOP
#I = 5, 5 = 5, EXIT AND MOVE ON

for i in range(4,12,2):
	#anything tabbed is considered the loop block.
	print(i)

print("*****BACKWARDS******")
#If you change your increment to go in reverse, the check is always i>check, in this case -1
for i in range(10,-1,-1):
	print(i)

print("Moving On")

print("****Printing String Characters****")
#We can use the loop to go through each index in a string to print out every letter.
#ALWAYS INDICATE THE LENGTH OF A WORD USING THE FUNCTION
#len
str = "Mo2322323nkey"
for i in range(0,len(str),1):
	print (str[i])

print("****Print string in reverse***")
for i in range(len(str)-1,-1,-1):
	print(str[i])

print("****Print Every Second LEtter in Str Start at Index 0***")
for i in range(len(str[1])1,1):
	print(str[i])
	