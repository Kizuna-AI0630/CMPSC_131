#1
'''
missing of apostrophe causing the output to be a mathmatic calculation
'''
#Fix: 
phoneNumber = '234-5678'
print('my phone number is ' + phoneNumber)

#2
print()
'''
missing of apostrophe causing error on output
'''
quote = 'I came to Casablanca for the waters.'
print(quote + ': '+'Bogart')

#3
print()
'''
Can not use a keyword as a variable name
'''
ffor = 'happily ever after.'
print('They lived ' + ffor)

#4
print()
print('python'[4])
print('Hello python!'[-9])
print('python'[0:3])
print('python'[:2])
print('python'[-3:2])
print('python'[2:-2])
print('python'[:])
print('python'[-2])
print('python'[5])
print('python'[2:2])
print('python'[2:])
print('python'[-5:-1])
print('python'[-4:4])
print('python'[-10:10])
print('python'.find('tho'))
print('python'.find('oh'))
print('python'.find('ty'))
print('python'.find('pyt'))
print()
print('Q23 Starts Here')
print('whizzbuzz'.rfind('zz'))
print(
'whizzbuzz'.find('zz'),
' Python'.lstrip(),
'hello_world'.startswith('hell'),
'smellElements'.capitalize(),
'hello_python'.rpartition('_'),
'PyThOn'.swapcase(),
'pyhton/java/c++'.split('/'),
'8 Ball'.title(),
len('brrr'),
'8 Ball'.upper(),
'whippersnapper'.count('pp'),
'python'[-1*len('Python')-1:3],
'python'.lower(),
'the artist'.title(),
len('Gravity    '.rstrip()),
len('Grand Hotel'[:6].rstrip()),
'king lear'.title(),
'let it go'.title().find('G'),
'Hello World!'.lower().find('wo'),
'Amazon'.lower().count('a')
     , sep='\n' )

#result
'''

>>> %Run 'W day4.py'
my phone number is 234-5678

I came to Casablanca for the waters.: Bogart

They lived happily ever after.

o
o
pyt
py

th
python
o
n

thon
ytho
th
python
2
-1
-1
0

Q23 Starts Here
7
3
Python
True
Smellelements
('hello', '_', 'python')
pYtHoN
['pyhton', 'java', 'c++']
8 Ball
4
8 BALL
2
pyt
python
The Artist
7
5
King Lear
7
6
2
>>> 

'''