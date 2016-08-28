weight = float(input('Enter your weight: '))
while (weight <= 0):
     print ('Invalid weight!')
     weight = int(input('Enter your weight? '))
else:
     print ('Your weight is: ')
     print(weight)