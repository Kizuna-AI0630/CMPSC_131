#1

num = int(input('Enter a positive number (negative to quit): '))
num1 = 0
if num != 0 and num > -1:
    while num > 0:
        num1  =num1 + num
        num = int(input('Enter a positive number (negative to quit): '))
    else:
        print('Total =', num1)
else:
    print('Enter a positive number to start. Restart the program!')

#2
'''
exitmsg = 'Done!'
password = input('Enter password: ')
while password != 'billgates' and password != 'quit':
    print('Incorrect password!')
    password = input('Try again, Enter password or type quit to exit: ')
print('Done!')
    '''

#2.1
exitmsg = 'Done!'
password = input('Enter password: ')
while password != 'billgates':
    print('Incorrect password!')
    password = input('Try again, Enter password or type quit to exit: ')
    if password == 'quit':
        print('Please Exit.')
        break # breaking command
if password == 'quit':
    exitmsg = 'You quit you Dumb'
    
    
#result
'''

>>> %Run 'W day13.py'
Enter a positive number (negative to quit): 2
Enter a positive number (negative to quit): 3
Enter a positive number (negative to quit): -1
Total = 5
Enter password: w
Incorrect password!
Try again, Enter password or type quit to exit: billgates
>>> 

'''