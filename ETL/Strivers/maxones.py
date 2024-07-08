a=[1,1,0,0,1,1,1,0,0,1,1,1,1]
maxcount=0
count=0
for i in range(len(a)):
    if a[i]==1:
         count=count+1
         maxcount=max(count,maxcount)
    else:
         count=0
print(maxcount)