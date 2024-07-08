#last index at which arr[x]>=k last occurance of the number


def upperbound(arr,k):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2
        if(arr[mid]<=k):
            low=mid+1
        else:
            high=mid
    return low

x=upperbound([1,3,3,5,7],3)
print(x)