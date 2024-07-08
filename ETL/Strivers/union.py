# pointer approach
a=[1,2,3,4,5,6]
b=[1,1,2,3,4,7,9]
c=[]
i=0
j=0
k=0
while(i<len(a) and j<len(b)):
    if(a[i]==b[j]):
        c.append(a[i])
        c.append(b[j])
        i=i+1
        j=j+1
    elif(a[i]>b[j]):
        c.append(b[j])
        j=j+1
    else:
        c.append(a[i])
        i=i+1
while(j<len(b)):
    c.append(b[j])
    j=j+1
while(i<len(a)):
    c.append(a[i])
    i=i+1
print(c)
