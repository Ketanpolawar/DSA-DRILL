


def mergeintervals(arr): 
    ans=[]
    j=0
    while j<len(arr):
        curr=arr[j]
        while(j<len(arr)-1 and curr[1]>=arr[j+1][0]):
            curr=[curr[0],max(curr[1],arr[j+1][1])]
            j=j+1
        ans.append(curr)
        j=j+1
    return ans

arr=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newarr=[4,8]
def insert(arr,newarr):
    arr.append(newarr)
    arr.sort(key=lambda x:x[0])
    pr=mergeintervals(arr)
    return(pr)
ans=insert(arr,newarr)
print(ans)