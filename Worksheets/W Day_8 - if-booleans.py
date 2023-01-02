#2
a = 1
b = 1.5
print(
    3 * a == 2 * b,
    ((5-a) * b) < 7,
    b <= 3,
    a ** b == b ** a,
    a ** (5-2) > 7,
    3e-2 < .01 * a,
    (a < b) or (b < a),
    (a * a < b) or not(a * a < a),
    not((a < b) and (a < (b + a))),
    not(a < b) or not (a < (b + a)),
    ((a == b) and (a * a < b * b)) or ((b < a) and (2 * a < b)),
    ((a == b) or not (b < a)) and ((a < b) or (b == a + 1)),
    sep = '\n'
    )
'''
True
True
True
False
False
False
True
True
False
False
False
True
'''
#3
print()
x = float(input('Enter the first number: '))
y = float(input('Enter the second number: '))
if x > y:
    print('The larger value is: ' + str(x))
elif x < y:
    print('The larger value is: ' + str(y)) 
else:
    print('They Are Equal')
#4
print()
s1 = input('Input a string: ')
l1 = list(s1)
l1.reverse()
l2 = ''.join(l1)
print(l2)

#result
'''

>>> %Run 'W day8.py'
True
True
True
False
False
False
True
True
False
False
False
True

Enter the first number: 1
Enter the second number: 2
The larger value is: 2.0

Input a string: hello
olleh
>>> 

'''