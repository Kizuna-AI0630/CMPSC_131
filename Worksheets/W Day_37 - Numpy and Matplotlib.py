import numpy as np
#1
a1 = np.arange(0,100)
print(a1)

#2
a2 = np.arange(1,101)
print(a2)

#3
A = np.arange(1,101,2)
print(A)
B = A[:10]
print(B)

#4
C = np.linspace(1,2,5)
print(C)

#5
A1 = np.array([1, 2, 4, 7]) 
A2 = np.array([12, 3, 6, 9])
print(A1+A2)
print(A1-A2)
print(A1*A2)

#6
TwoDArray = np.array([A1,A2])
print(TwoDArray)
print(TwoDArray.shape)

#7
import math
import matplotlib.pyplot as plt
t = np.arange(-math.pi,math.pi,0.2)
plt.plot(t,np.sin(t),'b--')
plt.plot(t,np.cos(t),'r--')
plt.axis([-4,4,-1,1])
plt.show()