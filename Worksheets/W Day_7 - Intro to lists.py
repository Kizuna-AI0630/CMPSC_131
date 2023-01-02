countries = [
    "Japan", "India", "Algeria", "Brazil", "Angola", "England", "Argentina",
    "Portugal", "China", "Australia", "Austria", "Ghana", "Bahamas", "Bangladesh", "Belgium",
    "Bhutan", "Bosnia", "Cameroon", "Canada", "Denmark"
    ]

countries1 = countries[:]
countries2 = countries[:]
countries3 = countries[:]
countries4 = countries[:]

#1
print(countries[2], countries[-1])
#2
print(countries[3], countries[-3])
#3
print(countries[18], countries[16])
#4
print(len(countries))
#5
print(countries[-1], countries[19])
#6
id1 = countries.index('Cameroon')
id2 = countries.index('Ghana')
print(str(id1) + ' ' + str(id2))
#7
print(countries[len(countries) - 1], countries[-1])
#8
print(countries[0].upper())
#9
countries1[0] = 'Jordan'
print(countries1)
print()
#10
countries2.insert(5, 'Germany')
print(countries2)
print()
#11
countries3.append('Nigeria')
print(countries3)
print()
#12
del countries4[4:6]
print(countries4)

#result
'''

>>> %Run 'W day7.py'
Algeria Denmark
Brazil Cameroon
Canada Bosnia
20
Denmark Denmark
17 11
Denmark Denmark
JAPAN
['Jordan', 'India', 'Algeria', 'Brazil', 'Angola', 'England', 'Argentina', 'Portugal', 'China', 'Australia', 'Austria', 'Ghana', 'Bahamas', 'Bangladesh', 'Belgium', 'Bhutan', 'Bosnia', 'Cameroon', 'Canada', 'Denmark']

['Japan', 'India', 'Algeria', 'Brazil', 'Angola', 'Germany', 'England', 'Argentina', 'Portugal', 'China', 'Australia', 'Austria', 'Ghana', 'Bahamas', 'Bangladesh', 'Belgium', 'Bhutan', 'Bosnia', 'Cameroon', 'Canada', 'Denmark']

['Japan', 'India', 'Algeria', 'Brazil', 'Angola', 'England', 'Argentina', 'Portugal', 'China', 'Australia', 'Austria', 'Ghana', 'Bahamas', 'Bangladesh', 'Belgium', 'Bhutan', 'Bosnia', 'Cameroon', 'Canada', 'Denmark', 'Nigeria']

['Japan', 'India', 'Algeria', 'Brazil', 'Argentina', 'Portugal', 'China', 'Australia', 'Austria', 'Ghana', 'Bahamas', 'Bangladesh', 'Belgium', 'Bhutan', 'Bosnia', 'Cameroon', 'Canada', 'Denmark']
>>> 

'''