#This program prints last digit of an entered integer

prompt = 'Please enter in an Integer: \n'

Int = input(prompt)

lastDigit = int(Int) % 10

print('Last Digit: ' + str(lastDigit))
