#1
'''
S = "What is your name?"
print(S[::2])
print(S[2:10:3])

Wa syu ae
aiy
'''

#2 Using a for loop create a list of letters from ‘a’ to ‘z’. The Unicode value of ‘a’ is 97 and ‘z’ is 122.
'''
l1 = []
for i in range (97,122+1):
    x = chr(i)
    l1.append(x)
print(l1)
'''

#3
'''
import string
user_input = input('here:')
punc = string.punctuation
whitsp = string.whitespace

l1 = user_input.split()
l2 = []
for a in range(0, len(l1)):
    x = l1[a] # x is not a list !!!
    if x[-1] in punc:
        l2.append(x[:-1])
    else:
        l2.append(x)
print(l2)
    '''