# brute fore requires the extra space count number append the non zeros and at last append the numeber of zeros
# optimal
a=[1,0,2,0,8]
i=0
count=0
for j in range(1,len(a)):
    if(a[j]!=0):
        i=i+1
        a[i]=a[j]
    if(a[j]==0):
        count=count+1
a=a[:i+1]
for i in range(count):
    a.append(0)
print(a)
# o(n) with no extra space