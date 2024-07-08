arr=[1,1,2,1,1]
oddcount=0
k=2
l=0
maxlength=0
for r in range(len(arr)):
    if arr[r]%2!=0:
        oddcount=oddcount+1
    while(oddcount>k and l<r):
       if arr[l]%2!=0:
           oddcount=oddcount-1
       l=l+1
    if(oddcount==k):
        maxlength=maxlength+1
print(maxlength)

