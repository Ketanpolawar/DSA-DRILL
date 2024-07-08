def Mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    Mergesort(arr,low,mid)
    Mergesort(arr,mid+1,high)
    Merge(arr,low,mid,high)

def Merge(arr,low,mid,high):
    left=low
    right=mid+1
    arr1=[]

    while(left<=mid and right<=high):
        if(arr[left]<=arr[right]):
            arr1.append(arr[left])
            left=left+1
        else:
            arr1.append(arr[right])
            right=right+1
    while left<=mid:
        arr1.append(arr[left])
        left=left+1
    while right<=high:
        arr1.append(arr[right])
        right=right+1
    for i in range(len(arr1)):
        arr[low+i]=arr1[i]


arr=[1,4,2,6,3,8,0]
Mergesort(arr,0,6)
print(arr)
