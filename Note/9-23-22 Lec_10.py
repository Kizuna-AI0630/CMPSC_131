#1 for loops

#1.1
for q in range(1,11):
    print(q*' ',q)
print('---------------------------------')
#1.2
for w in range(0,3):
    for e in range(5,6):
        print(w,e)
#2 time
import time

for r in range(1,10):
    print('*'*r)
    time.sleep(0.2)