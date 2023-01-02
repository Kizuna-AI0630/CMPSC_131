#1
# 65.43
print(format(65.4321, '.2f'))
print()

#2
# 987,654.13
print(format(987654.129, ',.2f'))

#3
num1 = 127.899
num2 = 3465.148
num3 = 0.3776
num4 = 264.821
num5 = 88.081
num6 = 799.999
print()
print(format(num1, '.2f'), format(num2, ',.2f'), format(num3, '.1%') , format(num4, '.2f'), format(num5, '.1f'), format(num6, '.2f'), sep='\n')

#4
print('One','Two','Three', sep = '*')
print('One','Two','Three', sep = '/')
print('One','Two','Three', sep = '\t')
print('One','Two','Three', sep = ':)')
print('One','Two','Three', sep = '')

#5
print()
five = 12233453
print(format(five,',.2f'), format(five,'e'), format(five,'.2e'), sep='\n')

#6
print()
mSalary = float(input('Enter Monthly Salary: '))
ySalary = format(mSalary*12, ',.2f')
print('Your annual pay is: $' + ySalary)

#result
'''

>>> %Run 'W day6.py'
65.43

987,654.13

127.90
3,465.15
37.8%
264.82
88.1
800.00
One*Two*Three
One/Two/Three
One	Two	Three
One:)Two:)Three
OneTwoThree

12,233,453.00
1.223345e+07
1.22e+07

Enter Monthly Salary: 100
Your annual pay is: $1,200.00
>>> 

'''


