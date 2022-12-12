#1
'''
str1 = input('here:')
def stringtolist(str1):
    l1 = []
    for i in range(len(str1)):
        a = str1[i]
        l1.append(a)
    print(l1)
stringtolist(str1)
'''
#2
'''
import string
user_input = 'Our grocery list is apples, bananas, and oranges.'
punc = string.punctuation

l1 = user_input.split()
l2 = []
for a in range(0, len(l1)):
    x = l1[a] # x is not a list !!!
    if x[-1] in punc:
        l2.append(x[:-2])
print(l2)
'''
#3
def employeeID():
    name1 = input()
    l1 = name1.split()
    l1.sort()
    l2 = []
    for i in range(1, len(l1)+1):
        l2.append(i)
    result = dict(zip(l1,l2))
    return result

print(employeeID())
