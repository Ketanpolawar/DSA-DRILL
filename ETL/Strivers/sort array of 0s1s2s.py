#count approach
count1=0
count0=0
count2=0
a=[1,0,2,0,1,0,2]
for i in range(len(a)):
    if(a[i]==1):
        count1=count1+1
    elif(a[i]==0):
        count0=count0+1
    else:
        count2=count2+1
for i in range(count0):
    a[i]=0
for i in range(count1):
    a[count0+i]=1
for i in range(count2):
    a[count0+count1+i]=2
print(a)