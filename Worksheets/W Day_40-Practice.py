'''
Write a program that displays two random numbers to
the use and asks for the result of the
product. The program congratulates the user if
the answer is right and ask to try again if its incorrect
'''

import random
def randNumMuti():
    num1 = random.randint(0,100000000)
    num2 = random.randint(0,100000000)
    print('What is the product of',num1,'and',num2,'(Type \'q\' to exit.)')
    answer = int(input('Answer = '))
    tries = 5
    while tries > -1 and answer != 'q':
        if tries > 0:
            if num1 * num2 == answer:
                print('Congraulation, you are correct! :)')
                break
            else:
                print('You are wrong, you have', tries , 'more chances, try again!')
                answer = int(input('Answer = '))
                tries -= 1
        else:
            print('You are done, try again next time!')
            break

randNumMuti()