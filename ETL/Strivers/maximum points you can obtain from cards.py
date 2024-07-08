arr=[1,2,3,4,5,6,1]
n=len(arr)
k=3
cs=0
for i in range(k):
    cs=cs+arr[i]
maxsum=cs

for i in range(1,k+1):
    cs=cs-arr[k-i]+arr[-i]
    maxsum=max(maxsum,cs)
print(maxsum)
