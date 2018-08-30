#Program Title: First and last Character of a string
#Program Description: Program asks for string from user and then
#                     prints the first and last character to the console


loop = ' '

def firstCharacter(string) :        #Function prints first character
    firstC = string[0:1]
    print("First Character: ", firstC)

def lastCharacter(string) :         #Function prints last character
    length = len(string)
    lastC = string[(length -1):length]
    print("Last Character: ", lastC)


while (loop != 'x') :
    s = input("Please input a string: ")
    print("\nString entered: ", s)
    firstCharacter(s)
    lastCharacter(s)

    print("\n\nWould you like to enter a new string?")
    loop = input("Select any key to continue or E(x)it: ")

    
    
