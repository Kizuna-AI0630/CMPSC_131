#1
'''
The error here is no 'self' in front of base in __init__ line.
no default parameter for base and altitutde
'''

#2
import circle 
c = circle.Circle() 
print(c.getRadius()) 
 
#3
c = circle.Circle() 
print(c.area()) 
 
#4
c = circle.Circle(4) 
print(c.getRadius()) 
 
#5
c = circle.Circle() 
c.setRadius(5) 
print(c.getRadius()) 
 
#6
c = circle.Circle(2) 
print(c.area()) 
 
#7
c = circle.Circle(3) 
print(c.circumference()) 
 
#8
c = circle.Circle() 
c.setRadius(3) 
print(c.circumference()) 
 
#9
c = circle.Circle() 
c.setRadius(2) 
print(c.area())

