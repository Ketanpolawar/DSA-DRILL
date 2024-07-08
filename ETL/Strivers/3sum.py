def triplets(arr):
    arr.sort()
    ans=[]
    n=len(arr)
    for i in range(arr):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=n-1
        while(j<k):
            total_sum=arr[i]+arr[j]+arr[k]
            if total_sum<0:
                j=j+1
            if total_sum>0:
                k=k-1
            else:
                temp=[arr[i],arr[j],arr[k]]
                ans.append(temp)
                j=j+1
                k=k-1
                while(j<k and arr[j]!=arr[j-1]):
                    j=j+1
                while(j<k and arr[k]!=arr[k+1]):
                    k=k-1
    return ans

