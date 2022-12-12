# Introduciton to Numpy
import numpy as np

#1
'''
np.array([1,4,2,5,3])

np.array([1,4,2,5,3], dtype=float32)
'''
#2
a = np.zeros(10, dtype=int) # It is int by default

b  = np.ones((3,5), dtype = float)

c = np.full((3,5), 3.14)

#3
d = np.arange(0,20,2)

e = np.linspace(0,1,5) #evenly spaced between 0 and 1

#4
np.eye(3)

np.empty(3)

#5
f = np.random.random((3,3))

g = np.random.normal(0,1,(3,3))

h = np.random.randint(0,10,(3,3))

#6
np.random.seed(0) #seed for reproducibility
x2 = np.random.randint(10,size=(3,4))

#7
'''
2D array
indexing:
x2[column, row]
'''