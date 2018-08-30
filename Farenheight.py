#Program Converts inputed Celsius temperature to Farenheight

prompt = ('Please input a Celsius temperature to convert\n')      #output to user
Celsius = input(prompt)

C = float(Celsius)          #String to float

F = (9/5)*C + 32            #Input into Farenheight Conversion formula
F = round(F,4)              #Rounds output to 5 digits

Farenheight = str(F)        #Convert float Farenheight to string

print(Celsius + ' degrees Celsius = ' + Farenheight + ' degrees Farenheight')
