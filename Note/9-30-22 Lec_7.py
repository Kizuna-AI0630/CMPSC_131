#1
'''
sentence = input('sentence: ')
letter = input('letter: ')
for i in range(0, len(sentence)):
    if sentence[i] != letter:
        print (sentence[i], end = '')
'''
#1.1
'''
def letter_remove (sentence, letter):
    for i in range(0, len(sentence)):
        if sentence[i] != letter:
            print(sentence[i], end = '')

sentence = input('sentence: ')
letter = input('letter: ')
letter_remove (sentence, letter)
'''

#2
'''
string = input('Enter a string: ')
letter = input('Enter a letter: ')
l1 = []
for i in range(0, len(string)) :
    if string[i] != letter:
        l1.append(string[i])
x = ''.join(l1)
print(x)
'''
#2.1
'''
def letter_remove1(string,letter):
    l1 = []
    for i in range(0, len(string)):
        if string[i] != letter:
            l1.append(string[i])
    x = ''.join(l1)
    print(x)

string = input('Enter a string: ')
letter = input('Enter a letter: ')
letter_remove1(string,letter)
'''
#3

def letter_remove (string, letter):
    l1 = list(string)
    for i in range(0, len(l1)):
        if 1[i] != letter:
            l1.remove(letter)
            
    y = ''.join(l1)
    print(y)

string = input('Enter a string: ')
letter = input('Enter a letter: ')
letter_remove (string, letter)
#If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.