a=[[1,3],[2,6],[8,10],[15,18]]
#sort the intervals
a.sort()
ans=[]
j=0
while j<len(a):
    curr=a[j]
    while(j<len(a)-1  and a[j+1][0]<=curr[1]):
        curr=[curr[0],max(a[j+1][1],curr[1])]
        j=j+1
    ans.append(curr)
    j=j+1
print("Merged intervals:", ans)



