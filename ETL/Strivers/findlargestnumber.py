#one time pass approach
ans=-float('inf')
a=[8,10,5,7,9]
x=len(a)
for i in a:
    if(i>ans):
        ans=i
print(ans)

#Complexity = O(N)



#sort and then get the last element
a.sort()
print(a[x-1])

#complexity N*LogN