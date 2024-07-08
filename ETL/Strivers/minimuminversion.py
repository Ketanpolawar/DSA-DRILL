#brutefore has O(n2) solution 

#optimized sountion 


def mergeinversion(low,high,arr):
    ct=0
    if(low>=high):
        return ct
    mid=(low+high)//2
    ct+= mergeinversion(low,mid,arr)
    ct+=mergeinversion(mid+1,high,arr)
    ct+=countinversion(low,mid,high,arr)
    return ct

def countinversion(low,mid,high,arr):
    left=low
    right=mid+1
    a=[]
    ct=0
    while(left<=mid and right<=high):
        if(arr[left]>arr[right]):
            ct=ct+(mid-left+1)
            a.append(arr[right])
            right=right+1
        else:
            a.append(arr[left])
            left=left+1
    while(left<=mid):
        a.append(arr[left])
        left=left+1
    while(right<=high):
        a.append(arr[right])
        right=right+1
    for i in range(len(a)):
        arr[low+i]=a[i]
    return ct
arr =  [5,4,3,2,1]
inversion_count = mergeinversion(0, len(arr) - 1, arr)
print(f"Number of inversions: {inversion_count}")
print(f"Sorted array: {arr}")