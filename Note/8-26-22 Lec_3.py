#1 round off
print(round(1.234567 , 2))

#2 the input function
birth_city = input('Enter the name of your city: ')
print('you are from ' + birth_city)

#2.1 convert int to str
age = 22
print('your age is ' + str(age))

#3 math library
import math
print(math.pi)
print(math.sqrt(9))

#4 Remember, by default input data will be String not a int even if it's a number

#5 Example
print()
age =  input('Enter your age: ')
print(type(age))

#5.1 convert to int
print()
age = int(input('Enter your age: '))
print(type(age))
print(age)
#Another way to do so
print()
age = (input('Enter your age: '))
print(type(age))
print(int(age)+2)
print()
#5.2 convert to float
weight = float(input('Enter your weight: '))
print(type(weight))
print(weight)