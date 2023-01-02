#1 Create a list of 100 zeros with a single line of code.
'''
print([0]*100)
'''

#2
# will not changed
'''
x1 = [1,2,3]
y1 = x1[:]
'''
# will changed
'''
x2 = [1,2,3]
y2 = x2
'''

#3
'''
x = 'abcde'
l1  = list(x)
l1[0] = 1
l1[2] = 'hello'
l1[3] = 15
l1.append('2')
print(l1)
'''

#4
def ssr(string): #string_sort_reverse
    list_str = list(string)
    list_str.sort()
    print(''.join(list_str))
string = input('here: ')
ssr(string)