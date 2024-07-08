arr=[1,0,2]
#give each chils one caondy
candy=[1]*len(arr)

#left to right checking
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        candy[i]=candy[i-1]+1
#right to left

for i in range(len(arr)-2,-1,-1):
    if arr[i]>arr[i+1]:
        candy[i]=max(candy[i],candy[i+1]+1)
print (sum(candy))
