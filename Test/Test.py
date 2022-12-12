'''
num = int(input('int = '))
for i in range (1,num+1):
    if i %3 ==0 and i %5 == 0:
        print('FizzBuzz')
    elif i %3 ==0 and i %5 != 0:
        print('Fizz')
    elif i %3 !=0 and i %5 == 0:
        print('Buzz')
    else:
        print(i)
'''
# input five number can be float and print sorted list sum and average with two decimal
l1 = []
for i in range(0,5):
        n = float(input())
        l1.append(n)
l1.sort() #sort method
Sum = format(sum(l1),'.2f')
Average = format(sum(l1)/5,'.2f')
print(l1)
print('Sum =', Sum)
print('Average =', Average)