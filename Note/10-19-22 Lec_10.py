l1 = [i for i in range(65,91)]

print(l1)

l2 = [chr(i) for i in range(65,91)]

print(l2)

D_codes = dict (zip(l2,l1))

print(D_codes)