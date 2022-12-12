#1 Give Initals
'''
name = input()
l1 = name.split()
print("Initials: ", end = '')
for i in range(0,len(l1)):
    a = l1[i]
    b = a[0]
    print(b+'.',end='')
    '''

#2 Classes
'''
class Book:
    def __init__(self, bTitle, auName, puName):
            self.bTitle = bTitle
            self.auName = auName
            self.puName = puName
    
    def set_bTitle(self, bTitle):
        self.bTitle = bTitle
    
    def set_auName(self, auName):
        self.auName = auName
        
    def set_puName(self, puName):
        self.puName = puName
    
    def get_bTitle(self):
        return self.bTitle
    
    def get_auName(self):
        return self.auName
    
    def get_puName(self):
        return self.puName
    
    def __str__(self): # 2 * '_' else will return number code
        return ('Title: ' + self.bTitle
                +'\nAuthor: ' + self.auName
                +'\nPublisher: ' + self.puName+'\n'
            )
####################################
Book_1 = Book('Educated', 'Tara Westover', 'Random House')
print(str(Book_1))
Book_2 = Book('A Brief History of Time','Stephen Hawking','Bantam Books')
print(str(Book_2))
####################################
'''
#3 Letter Frequency 'To fail to plan is to plan to fail.'
'''
user_input = input()
sentence = user_input.upper() # same case
letterDict = dict([(chr(n),0) for n in range(65, 91)]) #create an empy dictionary

for char in sentence:
    if 'A' <= char <= 'Z':
        letterDict[char] += 1

letterList = list(letterDict.items())
letterList.sort(key=lambda f: f[1],reverse=True) # sort the list by frequency

for x in letterList:
    if x[1] != 0:
        print(" " + x[0] + ':', x[1])
        '''

#4 Mutiply with recursion
'''
def product(x,y):
    if x == 0:
        return 0
    else:
        x -= 1
        return y + product(x,y)
    
        
num1 = int(input())
num2 = int(input())
print(num1,'times',num2,'is',product(num1,num2))
'''

#5 square of list
'''
def fsq(x):
    l1 = x
    l2 = []
    for i in range(len(x)):
        a = l1[i]*l1[i]
        l2.append(a)
    return l2


# DO NOT change the code below this line

s=input()
L1=list(map(lambda x: int(x),s.split(',')))

print(fsq(L1))
'''