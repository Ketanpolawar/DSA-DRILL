# simple loop first store leftmost then 0 yo n-1 i=i+1 place
a=[1,2,3,4,5]
temp=a[0]
for i in range(0,len(a)-1):
    a[i]=a[i+1]
a[len(a)-1]=temp
print(a)

# o(N)

# brute force extra array o(n) ,o(n)