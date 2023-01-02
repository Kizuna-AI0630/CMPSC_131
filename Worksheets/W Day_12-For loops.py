#1
num = int(input('Enter a non-negative integer: '))
if num > 0:
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    print(str(num) +'! is',fact)
else:
    print('0! is 1')
    
#2
import time
char = '*'
size = int(input('The number of rows and columns: '))
for r in range(size):
    for col in range(0,r):
        print(char, end = ' ')
        time.sleep(1)
    print()
#print one by one

#result
'''
>>> %Run 'W day12.py'
Enter a non-negative integer: 5
5! is 120
The number of rows and columns: 3

* 
* * 
>>> 

'''