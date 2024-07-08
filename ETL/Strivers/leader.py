arr=[1,2,3,4,5,6,7,8,9]
ans=[]
n=len(arr)
maxele=arr[n-1]
ans.append(arr[n-1])
for i in range(len(arr)-2,-1,-1):
    if(arr[i]>maxele):
        ans.append(arr[i])
        maxele=arr[i]
print(ans)

#last element is always leader
#initialise max as last element to comapre the other with it 
#if the element is greater than max add to answer and update max
        
