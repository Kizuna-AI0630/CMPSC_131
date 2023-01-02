import numpy as np
'''
#1
matrix = np.array([[5,8,2,0], [1, 1, 3,5], [3, 7, 9,2]])
#a
print(matrix.shape)

#b
print(matrix.size)

#c
print(matrix.ndim)

#d
print(matrix[2])

#e
print(matrix[:,1])

#f
print(matrix + 50)

#g
print(matrix.max())
print(matrix.min())

#h
print(matrix.mean())
print(matrix.std())
'''
#bones
'''
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)
'''

#2
a = np.zeros(15)
print(a)

#3
b = np.ones(9)
print(b)

#4
c = array=np.ones(7)*5
print(c)

#5
d = np.arange(0,36)
print(d)
d2 = d.reshape(6,6) # reshape array to a 6 by 6 dimensional array.
print(d2)
