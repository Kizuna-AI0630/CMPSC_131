#1
import math 
num1 = float(input('Enter a number: '))
if num1 > 0:
    result = math.sqrt(num1)
else:
    print('Number can’t be negative.')
print(format(result, '.2f')) # Remember do not put the print statement as part of the else block

#2
num2 = int(input('Enter a number from 1~7: '))
w_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

if num2 >= 1 and num2 <= 7:
    print(w_list[num2 - 1])
else:
    aErrorMsg = 'this is a number that is outside the range of 1 through 7'
    print(aErrorMsg.title())
#result
'''
#1
import math 
num1 = float(input('Enter a number: '))
if num1 > 0:
    result = math.sqrt(num1)
else:
    print('Number can’t be negative.')
print(format(result, '.2f')) # Remember do not put the print statement as part of the else block

#2
num2 = int(input('Enter a number from 1~7: '))
w_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

if num2 >= 1 and num2 <= 7:
    print(w_list[num2 - 1])
else:
    aErrorMsg = 'this is a number that is outside the range of 1 through 7'
    print(aErrorMsg.title())


'''