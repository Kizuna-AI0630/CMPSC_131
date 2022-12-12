#1
'''
Write a program to determine if a customer qualifies for a loan.
The program should take two input values as floats:
First one should be salary and the second one should be the years on the job.
In order to qualify for the loan the minimum salary is 30,000$ and the minimum number of years is on the job is 2.

salary = float(input())
years = float(input())

if salary >= 30000 and years >= 2:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')
    '''
#2
'''
Sentence Reverse

sentence = input()
l1 = sentence.split()
x = l1.reverse()
print(x)
'''

#3
'''
totalSales = 0 # define inital value
for i in range(7):
    numSales = float(input())
    totalSales = totalSales + numSales # Stack up
print('Total sales: $' + str(format(totalSales,',.2f')))
print('Average Daily: $' + str(format(totalSales/7,',.2f')))
'''

# Extra
'''
1) reverse
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

['Volvo', 'Ford', 'BMW']

2) Sort the list by the length of the values:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)

['VW', 'BMW', 'Ford', 'Mitsubishi']

3)
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

4)
The sort() method sorts the list ascending by default.

'''