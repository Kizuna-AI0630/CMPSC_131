#1
'''
my_set =set( 'bcd')
your_set = set('abcde')
print(my_set.issubset(your_set)) # true
print(your_set.issubset(my_set)) # false
'''
#2
l1 = []
a_set = set('pepper')
for element in a_set:
    a = element
    l1.append(a)
l1.reverse()
x = ''.join(l1)
print(x)

#3
'''
aset={"A", "B", "C", "D"}
bset={"G", "B", "C", "H"}
#1.1
print(aset|bset)
#1.2
print(aset & bset)
#1.3
print(aset - bset)
print(bset - aset)
#1.4
print(aset ^ bset)
'''