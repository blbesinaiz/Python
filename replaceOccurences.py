#Program Title: Replace Occurences
#Program Description: Program takes in a string, and all occurences of its 
#                     first char have been changed to '$', except the first
#                     char itself




def replaceInstance(s) :
    char = '$'
    firstC = s[0:1]

    i = 1

    while i < len(s):
        letter = s[i]
        if(letter == firstC) :
            s = s[:i] + char + s[i + 1:]
        i += 1

    return s

string = input("Please enter a string: ")
print("String Entered: ", string)

replacedStr = replaceInstance(string)
print("Replaced String: ", replacedStr)
    
