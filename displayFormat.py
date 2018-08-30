#Program Title: Formatted Display
#Program Description: Program takes in a string, and outputs the text 
#                     with a width of 50

import sys

string = input("Please enter a string: ")

for i in range(10):
    sys.stdout.write('['+str(i)+']')

print(string)
