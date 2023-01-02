#1
'''
def word_count(msg):
    if len(msg) <= 160:
        return msg
    else:
        x = msg[0:160]
        print('Program only accept the first 160 characters.'.title())
        print('---'*100)
        return x

msg = input('Enter a here: ')
print(word_count(msg))
'''

#2
def list_product(numInput):
    l1 = numInput.split()
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    result = 1
    for x in l1:
        result = result * x
    print("Product = ", result)

numInput = input('Enter number(s) separated by space: ')
list_product(numInput)