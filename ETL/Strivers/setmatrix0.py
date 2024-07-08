#using rows and cols array
arr=[[1,1,1],[1,0,3],[3,4,1]]
rows=[0]*len(arr)
col=[0]*len(arr[0])

for i in range (len(arr)):
    for j in range(len(arr[0])):
        if(arr[i][j]==0):
            rows[i]=1
            col[j]=1

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if rows[i] or col[j]:
            arr[i][j]=0
print(arr)
