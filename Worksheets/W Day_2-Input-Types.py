#1
'''
it will print out -8, 26.4, 10.14
'''
x = 5 
y = 7 
print (abs(x - y) - 10) 
print (int(x ** 2) + 1.4) 
print(round(y + 3.14159, 2))

#2
'''
In Python, string literals are surrounded by single quotes or double quotes
'''

#3
''' X-ray will be a invaild variable name '''

#4
'''
The default number of decimals is 0, meaning that the function will return the nearest integer.

If the value of n is 3.14159, the function round(n) will return 3
'''
print(round(3.15159))

#5 Calculate a company’s profit
print()
revenue  = 98456
costs  = 45000
profit = revenue - costs
print(profit)

#6 Give the name and birth year of a famous inventor
firstName = 'Thomas '
middleName = 'Alva '
lastName = 'Edison '
yearOfBirth = 1847
print("The year of birth of " + firstName + middleName + lastName + 'is ' + str(yearOfBirth))

#7 Calculate price of ketchup
item = 'ketchup'
regularPrice = 1.8
discount = .27
finalPrice = regularPrice - discount
print(str(finalPrice) + ' is the sale price of ' + item)

#8 Calculate the area of a circle
import math
radius = float(input('Enter the radius of the circle: '))
area = math.pi * radius ** 2
print('The area of the circle with radius ' + str(radius) + ' is: ' + str(area))
#Remember to convert all the int and float to str when adding them together ! ! !

# result
'''
>>> %Run 'W day2.py'
-8
26.4
10.14
3

53456
The year of birth of Thomas Alva Edison is 1847
1.53 is the sale price of ketchup
Enter the radius of the circle: 

'''
