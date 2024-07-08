def febo(n):
    if n == 0 or n == 1:
        return n
    else:
        return febo(n-1) + febo(n-2)

m = 10
for i in range(m):
    print(febo(i))
