arr=[900,945,955,1100,1500,1800]
arr2=[920,1200,1130,1150,1900,2000]

arr.sort()
arr2.sort()
i=1
j=0
cs=1
maxcs=1
while(i<len(arr) and j<len(arr)):
    if(arr2[j]>=arr[i]):
        cs=cs+1
        maxcs=max(maxcs,cs)
        i=i+1
    else:
        cs=cs-1
        j=j+1
print(maxcs)

