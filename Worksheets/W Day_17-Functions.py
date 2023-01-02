#1 Fibonacci sequence
'''
def fibonacci_sequence(num):
        l1 = [0,1]
        for i in range(2,num):
            x = l1[i-1] + l1[i-2]
            l1.append(x)
        return(l1)
num = int(input('Prints the first N numbers of the Fibonacci sequence. N = '))
print(fibonacci_sequence(num))
'''
#1.1 Not using list
a = 0
b = 1
num = int(input('Prints the first N numbers of the Fibonacci sequence. N = '))
print(a,b,'',end='')
for i in range(num-1):
    c = a + b
    print(c,end =" ")
    b = a
    a = c
#2 Palindrome
'''
#the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1
def palindrome(string):
    org = list(string)
    l1 = list(string) # turn into a list
    l1.reverse()
    if l1 == org:
        print('is a palindrome'.title())
    else:
        print('is not a palindrome'.title())

palindrome(input('Input a string here to determine if it\'s a palindrome: '.title()))
'''