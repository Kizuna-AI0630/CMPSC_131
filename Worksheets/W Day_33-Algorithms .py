#1
def dupcount(l1):
    count = 0
    for i in range (0,len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i] == l1[j]:
                count +=1
    return count
    
length = int(input('Lengths of the sequence: '))
list2 = []
for o in range(0,length):
    nums = int(input('Enter a num: '))
    list2.append(nums)
    
print(dupcount(list2))
    