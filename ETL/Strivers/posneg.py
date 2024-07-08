a = [1, 2, 3, -1, -2, -3]
b = [0] * len(a)
posindex = 0
negindex = 1

i = 0
while i < len(a):
    if a[i] > 0 and posindex < len(a):
        b[posindex] = a[i]
        posindex += 2
    elif a[i] < 0 and negindex < len(a):
        b[negindex] = a[i]
        negindex += 2
    i += 1

print(b)
