#1  Convert percentage to decimal
percentage = int(input('Enter percentage: '))
decimal = percentage / 100
print('Equivalent decimal: ' + str(decimal))
print()

#2  A program to request a person’s age and resting heart rate and display their raining heart rate. 
age = int(input('Enter your age: '))
rHeartR = int(input('Enter your resting heart rate: ')) #rHeartR = resting heart rate
tHeartR = .7*(220 - age) + .3 * rHeartR #tHeartR = training heart rate
print('Training heart rate: ' + str(tHeartR) + ' beats/min.')
print()

#3
first = int(input('Please enter first interger: '))
second = int(input('Please enter second interger: '))
tSum = first + second
tProduct = first * second
tDifference = first - second
tQuotient = first / second
tRemainder = first % second
print('Sum = ' + str(tSum),
      'Product = ' + str(tProduct),
      'Difference = ' + str(tDifference),
      'Quotient = ' + str(tQuotient),
      'Remainder = ' + str(tRemainder),
      sep = '\n'
      )

#result
'''

>>> %Run 'W day3.py'
Enter percentage: 5
Equivalent decimal: 0.05

Enter your age: 5
Enter your resting heart rate: 4
Training heart rate: 151.7 beats/min.

Please enter first interger: 5
Please enter second interger: 4
Sum = 9
Product = 20
Difference = 1
Quotient = 1.25
Remainder = 1
>>> 

'''