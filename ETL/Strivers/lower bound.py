#first index where value at x is greater than k first occurance of number
def lowerbound(arr,k):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2
        if(arr[mid]<k):
            low=mid+1
        else:
            high=mid
    return low

x=lowerbound([1,3,3,5,7],3)
print(x)