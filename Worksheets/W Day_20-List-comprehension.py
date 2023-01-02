#1
# print([(n*n) for n in range(13) if (n*n)%2==0] )
#[0, 4, 16, 36, 64, 100, 144]

#2
Q = [1,5,3,6,2,9,7,8,0]
#2.1 find the sum of the even integers in list L
print(sum([i for i in Q if i %2 == 0]))
print()
#2.2 find the sum of the odd integers in list L
print(sum([i for i in Q if i %2 == 1]))
print()
#3
x= 'January 1, 2000'
print(''.join([a for a in x if a.isalpha()]))