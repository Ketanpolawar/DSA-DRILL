def subarray(arr,k):
    nums=arr
    l=0
    ans=0
    counter={}
    for r in range(len(arr)):
        if(nums[r] in counter):
            counter[nums[r]]+=1
        else:
            counter[nums[r]]=1
        while(len(counter)>k ):
            if(counter[nums[l]]==1):
                del counter[nums[l]]
            else:
                counter[nums[l]]-=1
            l=l+1
        ans=ans+(r-l+1)
    return ans
arr=[1,2,1,2,3]
k=2
result=(subarray(arr,k)-subarray(arr,k-1))
print(result)


        