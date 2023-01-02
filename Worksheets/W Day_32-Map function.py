#1
'''
import random
l1 = [random.randint(97,120) for i in range(20)]
print(list(map(lambda x : chr(x), l1)))
print(list(map(lambda x : chr(x+2), l1)))
'''

#2
'''
def sumsq(*nums):
    l2 = []
    for num in nums:
        num = num**2
        l2.append(num)
    print(sum(l2))

sumsq(1,2,3,4,5,6,7,8,9,10,11,12)
'''

#2.1
def sumsq(*nums):
    l1 = (list(map(lambda num : num**2, nums)))
    a = sum(l1)
    print(a)
sumsq(1,2,3)
    