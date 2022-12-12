#1
'''
str1 = 'Incomprehensibilities'

s1 = str1[2:10]
print(s1)
l1 = []
for i in range(len(s1)):
    a = s1[i]
    l1.append(a)
l1.reverse()
x = ''.join(l1)
print(x)
'''
#2
'''
s1 = 'The pen is mightier than the sword'
l1 = s1.split()
for i in range(0,len(l1)):
    a = l1[i]
    x = a[0]
    y = a[len(a)-1]
    z = a[1:len(a)-1]
    word2 = y+z+x
    print(word2, end=' ')
'''
#3
s1 = 'see the bright side'
l1 = s1.split()
l2 = []
for i in range(len(l1)):
    x = len(l1[i])
    l2.append(x)
result = zip(l1,l2)
print(dict(result))