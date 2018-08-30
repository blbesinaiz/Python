#Write a program that determines the Letter Grade of a decimal entered

#Prompt user to input a number
userGrade = int(input('Please enter a grade ex. 89: \n'))
                  
#Convert to decimal
Grade = userGrade/100
                  

#if statements to determine Lettter grade
if(Grade < 0 or Grade > 1) :
    letter = 'Invalid input!!'
elif(Grade >= .90) :
   letter = 'A'
elif(Grade <= .89 and Grade >= .80) :
    letter = 'B'
elif(Grade <= .79 and Grade >= .70) :
    letter = 'C'
elif(Grade <= .69 and Grade >= .60) :
    letter = 'D'
elif(Grade < 60) :
    letter = 'F'

print('Letter grade equivalent: ', letter)
