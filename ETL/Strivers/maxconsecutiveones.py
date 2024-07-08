#longest subarry with atmost k zeros

arr=[1,2,0,0,3,4,0,0,8,9,7,0]
sun=[]
l=0
zeros=0
k=2
maxlen=0
for r in range(len(arr)):
    if(arr[r]==0):
        zeros=zeros+1
    while(zeros>k):
        if arr[l]==0:
            zeros-=1
        l=l+1
    maxlen=max(maxlen,r-l-1)
print(maxlen)


