#first find the solution for the subarray less than  equal to k 
#also conut is increased by r-l-1(consider alll the subarry)
#call this function for goal and gaol-1

def leass(arr,k):
    l=0
    cs=0
    ct=0
    for r in range(len(arr)):
        cs=cs+arr[r]
        while(cs>k and l<=r):
            cs=cs-arr[l]
            l=l+1
        ct=ct+(r-l+1)
    return ct

arr=[1,0,1,0,1]
k=2
print(leass(arr,k)-leass(arr,k-1))

    