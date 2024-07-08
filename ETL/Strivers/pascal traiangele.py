#pascals triange
n=5
arr=[[0]*(i+1) for i in range(n)]
arr[0][0]=1
for i in range (1,n):
    arr[i][0]=1
    for j in range(1,i):
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    arr[i][i]=1
print(arr)
print(arr[4][2])
print(arr[2])
