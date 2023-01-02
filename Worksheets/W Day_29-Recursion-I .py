#1
def Sum(n):
    if n == 1:
        return n
    else:
        return n + Sum(n-1)
n = int(input('Enter a number n to find the sum 1+2+3+...+n: '))
print('Sum = ', str(Sum(n)))

#2
def fat(n):
    if n == 1:
        return n
    else:
        return n * fat(n-1)
n = int(input('Enter a number n to find the sum 1+2+3+...+n: '))
print('Factorial = ', str(fat(n)))