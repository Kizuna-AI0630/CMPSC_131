
#1 Area of a circle
def area_circle(radius):
    return 3.14 * radius ** 2

radius = float(input('Enter the radius: '))
print(area_circle(radius))

#2 Energy mass relation
def nrg_equv(mass):
    c = 3e8
    return mass * c **2
mass = float(input('Enter the mass: '))
print(nrg_equv(mass))

#3 Score comparison
def comp_score(team1,team2):
    if team1 > team2:
        return 'team 1 won'
    elif team1 < team2:
        return 'team 2 won'
    else:
        return 'Tied'
team1 = int(input('Enter the team 1 score: '))
team2 = int(input('Enter the team 2 score: '))
print(comp_score(team1,team2))

#result
'''
>>> %Run 'W day14.py'
Enter the radius: 2
12.56
Enter the mass: 3
2.7e+17
Enter the team 1 score: 2
Enter the team 2 score: 3
team 2 won
>>> 

'''