#1
temp_file = open('my_name.txt', 'w')
print('Hao Wang' , file=temp_file)
temp_file.close()

#2
temp_file = open('my_name.txt', 'r')
lines = temp_file.read()
print(lines)
temp_file.close

#3
temp_file = open('number_list.txt', 'w')
x = 1
while x <101:
    print(x, file=temp_file)
    x += 1
temp_file.close()
