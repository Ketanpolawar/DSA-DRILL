arr=[1,2,43,5,7,6,9]

#selection sort

for i in range(len(arr)):
    mi=i
    for j in range(i,len(arr)):
        if(arr[j]<arr[mi]):
            mi=j
    arr[mi],arr[i]=arr[i],arr[mi]
print(arr)


arr=[2,4,7,5,8,6]
#insertion sort

for i in range(1,len(arr)):
    j=i
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j=j-1
print(arr)


arr=[3,7,4,9,7]
#bubblesort

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)