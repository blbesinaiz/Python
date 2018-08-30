#Write a program to calculate a person's age

import datetime

stop = ' '

while (stop != 'X') :

    birthYear = int(input('Please enter your birth year ex. 2000\n'))
    birthMonth = int(input('Please enter your birth month ex. 07\n'))
    birthDate = int(input('Please enter your birth day ex. 14 \n'))

    now = datetime.datetime.now()   #Get current Date
    currentYear = now.year          #Set year 
    currentMonth = now.month        #Set Date
    currentDay = now.day            #Set Day

    yearAge = currentYear - birthYear     #Compute current year

    if(birthMonth > currentMonth) :       #If birthmonth hasn't come yet
        yearAge = yearAge - 1

    elif(currentMonth == birthMonth and birthDate > currentDay) :   #Compare by day
        yearAge = yearAge -1


    print('Current Age: ', yearAge)
    
    print('\nWould you like to try a new age calculation?')
    stop = str(input('Press ANY KEY to continue or X to Exit\n'))

    if (stop == 'X') :
        break
