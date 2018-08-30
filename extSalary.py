#From the information obtained, calculate Gross Pay, Taxes, and Net Pay
print('This program will calculate an employees Gross Pay, Net Pay, and Tax Rate\n')

promptHours = 'Please enter hours worked: \n'
hours = float(input(promptHours))

promptPayrate = 'Please enter hourly wage: \n'
payRate = float(input(promptPayrate))

promptTaxrate = 'Please enter tax rate percentage(ie 2.5): \n'
taxRate = float(input(promptTaxrate))

OverPay = 0
OverH = 0

if(hours <= 40) :
    print('Computations for Employee with no overtime: \n')
    grossPay = hours * payRate

else :
    print('Computations for Employee with overtime: \n')
    OverH = hours - 40
    OverPay = OverH * (payRate * 1.5)
    grossPay = (hours + OverPay) * payRate

taxRate = (taxRate/100) * grossPay      #Turn into decimal
netPay = (grossPay) - (taxRate)

print('Hours Worked: ' + str(hours) + '   ' + 'Over Time Hours: ' + str(OverH))
print('Over Time Additional Pay: ' + str(OverPay))
print('Grosspay: $' + str(grossPay) + '\n')           #need to set precision
print('Taxrate: $' + str(taxRate) + '\n')
print('Netpay: $' + str(netPay) + '\n')





      
