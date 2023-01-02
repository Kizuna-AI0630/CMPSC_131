#1
'''
n = int(input('Enter the length of the Seq: '))
l1=[]
for i in range(n):
    l1.append(int(input('Enter a number to add to Seq: ')))

for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print(l1)
'''
#2
def bubblesort(l2): 
    n = len(l2)
    print(l2)
    for i in range(n):
        print('Pass =',i+1)
        
        for j in range(0,n-i-1):
            if l2[j] > l2[j+1]:
                l2[j], l2[j+1] = l2[j+1], l2[j]
            print(l2)
   
    return l2
    
n = int(input('Enter the length of the Seq: '))
l2=[]
for i in range(n):
    l2.append(int(input('Enter a number to add to Seq: ')))

bubblesort(l2)