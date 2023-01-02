#1 Age Classifier
age = int(input('Enter age: '))
if age <= 1:
    print("Infant")
elif age>1 and age<13:
    print('Child')
elif age>=13 and age<20:
    print('Teenager')
elif age>=20:
    print('Adult')
print()

#2 Mass and Weight
mass = int(input("Enter the object's mass in kilograms:"))
weight = mass * 9.8
if weight > 500:
    print('The object is too heavy. It weighs more than 500.0 Newtons. ')
elif weight < 100:
    print('The object is too light. It weighs less than 100.0 Newtons.')
else:
    print('The object is good. It weighs in the range of 100.0~500.0 Newtons.')
print()

#3
for x in range(0, 101, 2): # The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter
  print(x)
  
#result
  '''
>>> %Run 'W day10.py'
Enter age: 23
Adult

Enter the object's mass in kilograms:32
The object is good. It weighs in the range of 100.0~500.0 Newtons.

0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
>>> 

'''