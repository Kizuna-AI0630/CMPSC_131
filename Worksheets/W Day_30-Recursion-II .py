#1
'''
def fib(n):
    if n == 0 :
        return n
    elif n ==1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input('N ='))+1
print(fib(n))
'''

#2
def draw(n):
    if n == 0:
        return
    else:
        print('*' * n)
        draw(n-1)
n = int(input('N ='))
draw(n)

#2.1 Not HW
def draw(n):
    if n == 0:
        return
    else:
        draw(n-1) # recursion will return to the interupted line
        print('*' * n)
n = int(input('N ='))
draw(n)