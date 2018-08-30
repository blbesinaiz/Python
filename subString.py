#Program Title: Substring
#Program Description: Takes the a string from the user and outputs three
#                     characters from the middle

s = input("Please input a string: ")
section = int(input("Please input the size of the slice (i.e 3)"))

length = len(s)             #Gets length of string
middle = int(length/2)      #Gets middle value of string
incr = int(section/2)       #Decides how much deviation from middle

subString = s[middle - incr:middle + incr]      #Prints middle sub string

print("The sub string selected: ", subString)   #Prints middle of string
