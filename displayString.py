#Program Title: Display String
#Program Description: Program takes in a string, asks the user to enter the
#                     character to to count, and then outputs the number of
#                     occurences

string = input("Please enter a string: ")
char = input("Please enter a character to count: ")

value = string.count(char)

print("The number of times (", char, ") occurs is: " ,value)
