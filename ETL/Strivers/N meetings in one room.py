start=[10,12,20]
end=[20,25,30]
n=[0,1,2]

count=1 #consider that first meeting can alwys be done
limit=end[0]
#sort in ascending order of finish time
for i in range(1,len(end)):
    j=i
    while j>0 and end[j-1]>end[j]:
        end[j-1],end[j]=end[j],end[j-1]
        start[j-1],start[j]=start[j],start[j-1]
        n[j-1],n[j]=n[j],n[j-1]
        j=j-1
for i in range(1,len(end)): #start from second meeting
    if(start[i]>limit):
        count=count+1
        limit=end[i]
print(count)


