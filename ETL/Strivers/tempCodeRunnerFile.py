a=[[1,3],[2,6],[8,10],[15,18]]
a.sort()
ans=[]
j=0
while j<len(a):
    curr=a[j]
    while(a[j+1][0]<=curr[1] and j<len(a)-1):
        curr=[a[j][0],max(a[j+1][1],curr[1])]
        j=j+1
    ans.append(curr)
    j=j+1