#recursive approach

# def binarysearch(low,high,arr,k):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if(arr[mid]==k):
#         return mid
#     elif(arr[mid]<k):
#         return binarysearch(mid+1,high,arr,k)
#     elif(arr[mid]>k):
#         return binarysearch(low,mid-1,arr,k)


#iterative approach

def binarysearch(arr,k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid
        elif(arr[mid]>k):
            high=mid-1
        else:
            low=mid+1
    return -1


#if search space is intmax tjhen use long or assigh low= low-(high-low)/2