def dividepairs(arr,low,high):
    ct=0
    if low>=high:
        return ct
    mid=(low+high)//2
    ct=ct+dividepairs(arr,low,mid)
    ct=ct+dividepairs(arr,mid+1,high)
    ct=ct+merge(arr,low,high,mid)
    return ct
def merge(arr,low,mid,high):
    ct=0
    left=low
    right=mid+1
    ans=[]
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        ct=ct+right-(mid+1)
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(arr[left]>arr[right]):
            ans.append(arr[right])
            right=right+1
        else:
            ans.append(arr[left])
            left=left+1
    while(left<=mid):
        ans.append(arr[left])
        left=left+1
    while(right<=high):
        ans.append(arr[right])
        right=right+1
    for i in range(len(ans)):
        arr[low+i]=ans[i]
    return ct
