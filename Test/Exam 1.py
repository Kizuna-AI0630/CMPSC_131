#1
'''
pangram = "The quick onyx goblin jumps over the lazy dwarf"

# Enter your code here. 
letter = input()
x = pangram.index(letter)
print('The index of ' + letter + ' is ' + str(x))
'''
#2 Education: the path from cocky ignorance to miserable uncertainty.
'''
sentence = input('here:')
l1 = sentence.split(' ') # convert into a list
l2 = []
for i in range(0,len(l1)):
    if len(l1[i]) <= 3:
        l2.append(l1[i])
print(l1)
for i in range(0,len(l2)):
    print(l2[i])
'''
sentence = input('here:')
l1 = sentence.split(' ') # convert into a list
l2 = []
for i in range(0,len(l1)):
    if len(l1[i]) <= 3:
        l2.append(l1[i])
print(l1)
print(l2, sep = '\n')

