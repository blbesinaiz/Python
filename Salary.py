#From the information obtained, calculate Gross Pay, Taxes, and Net Pay

print('This program will calculate an employees Gross Pay, Net Pay, and Tax Rate\n')

promptHours = 'Please enter hours worked: \n'
H = input(promptHours)

promptPayrate = 'Please enter hourly wage: \n'
P = input(promptPayrate)

promptTaxrate = 'Please enter tax rate percentage(ie 2.5): \n'
T = input(promptTaxrate)

grossPay = float(H) * float(P)
grossOut = round(grossPay, 2)            #Should round to 2 decimal places
taxRate = (float(T)/100) * grossPay      #Turn into decimal
taxOut = round(taxRate, 2)
netPay = (grossPay) - (taxRate)
netOut = round(netPay, 2)

print('Grosspay: $' + str(grossPay) + '\n')           #need to set precision
print('Taxrate: $' + str(taxOut) + '\n')
print('Netpay: $' + str(netOut) + '\n')
