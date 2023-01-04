#1
try: 
  x = float('abc123') 
  print('The conversion is complete.') 
except IOError: 
  print('This code caused an IOError.') 
except ValueError: 
  print('This code caused a ValueError.') 
print('The end.')
### This code caused a ValueError. ###

#2
try: 
  x = float('abc123') 
  print(x) 
except IOError: 
  print('This code caused an IOError.') 
except ZeroDivisionError: 
  print('This code caused a ZeroDivisionError.') 
except: 
  print('An error happened.') 
print('The end.')
### An error happened. ###

#3
try:
    temp_file = open('Ages.txt','r')
    lines = temp_file.read()
    print('Ages: ' + lines)
    temp_file.close
except FileNotFoundError:
    print('File Ages.txt not found.')
except ValueError:
    print('File Ages.txt contains an invalid age.')
except: 
  print('An error happened.') 
print('The end.')