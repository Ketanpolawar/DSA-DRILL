a=[1,3,2,5,4,6,8,7]
min_index=0#min index
for i in range (len(a)):
    min_idx=0
    for j in range(i+1,len(a)): #innner lope from remaining element
        if(a[min_idx]<a[j]):
            min_idx=j
        temp=a[min_idx]
        a[min_idx]=a[j]
        a[j]=temp
print(a)

#find the min from remaining positions
#swap min with current index