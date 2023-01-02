#1
'''
D = {'a': 10, 'b': 20, 'c': 30}
print('key     value')
for key, value in D.items(): print(key, '\t',value)
'''
#2
#1)
'''
D = {'a':3, 'x':7, 'r':5}
key = input('key: ')
print(D[key])
'''
#2)
a = int(input('num here: '))
D = {'a':3, 'x':7, 'r':5}
for key, value in D.items():
    if a == value:
        print(key)

#3)
'''
D = {'a':3, 'x':7, 'r':5}
D['z'] = 10
print(D)
'''
#4)
'''
D = {'a':3, 'x':7, 'r':5}
del D['a']
print(D)
'''