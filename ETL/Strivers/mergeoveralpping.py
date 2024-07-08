arr=[[1,3],[2,6],[8,10],[15,18]]
arr.sort(key=lambda x:x[0])
i=0
ans=[]
while(i<len(arr)):
    curr=arr[i]
    while(i<len(arr)-1 and curr[1]>=arr[i+1][0]):
        curr=[curr[0],max(curr[1],arr[i+1][1])]
        i=i+1
    ans.append(curr)
    i=i+1
print(ans)
    
    
