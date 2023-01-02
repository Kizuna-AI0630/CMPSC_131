#1 Replacing method
str1 = 'Here are a string'
str2 = str1.replace('are', 'is')
print(str2)

#1 String Slicing
str1 = 'Here are a string'
print(str1[0:5]+ 'is' +str1[-9:])

#2
# Franklin Delano Roosevelt
fullName = input('Enter a full name: ')
index = fullName.rfind(' ')
lastName = fullName[int(index)+1: ]
firstName = fullName[:index]
print('Last Name: ' + lastName,'First name(s): ' + firstName, sep='\n')

# result
'''

>>> %Run 'W day5.py'
Here is a string
Here is a string
Enter a full name: hao wang
Last Name: wang
First name(s): hao
>>> 

'''
