#1
f1 = lambda m : m*(3e8 ** 2)
print(f1(10))

#2
f2 = lambda l1 : sum(l1)/len(l1)
l1 = [1,2,3,4]
print(f2(l1))

#3
list1 = ['c', 'D', 'a', 'B']
print(sorted(list1, key=lambda x : x.lower()))

# sorted_list = sorted(unsorted_list, key=lambda s: s.lower())

# sorted_list = sorted(unsorted_list, key=str.casefold)