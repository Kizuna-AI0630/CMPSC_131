my_dict = {'a':20 , 'c':35, 'b':15}
#1
'''
for key, value in my_dict.items(): print(key, end = ' ')
print()

#2
for key, value in my_dict.items(): print(value, end = ' ')
print()

#3
for key, value in my_dict.items(): print(key, '\t',value)
'''
#4
'''
print(sorted([(key, value) for key, value in my_dict.items()]))
'''
#5
'''
print(sorted([(value,key) for key, value in my_dict.items() ]))
'''

#6
F1 = ['Jane', 'John', 'Jack']
L2 = ['Doe', 'Deer', 'Black']
D_codes = dict(zip(F1,L2))
print(D_codes)