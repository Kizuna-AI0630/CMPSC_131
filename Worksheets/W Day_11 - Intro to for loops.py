#1
totalBooks = 0 # define inital value
for i in range(5):
    numBooks = int(input('Enter the number of books collected today: '))
    totalBooks = totalBooks + numBooks # Stack up
print('Total books collected: ' + str(totalBooks))
print()

#2
#initialBurn = 0
print('Minutes','\t','Calories Burned')
for minutes in range(10,31,5):
    caloriesBurned = minutes * 4.2
    print(minutes, ' '*19 ,caloriesBurned)


#result
'''
>>> %Run 'W day11.py'
Enter the number of books collected today: 2
Enter the number of books collected today: 3
Enter the number of books collected today: 4
Enter the number of books collected today: 5
Enter the number of books collected today: 6
Total books collected: 20

Minutes 	 Calories Burned
10                     42.0
15                     63.0
20                     84.0
25                     105.0
30                     126.0
>>> 

'''