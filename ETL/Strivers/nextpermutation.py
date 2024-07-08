#find the break point
#from right od breakpoint fin min index
#swap with the min index 
#now reverse the right of break point
#if no break point return same array

a=[2,1,5,4,3,0,0]
bp=-1
for i in range(len(a)-1,-1,-1):
    if(a[i]>a[i-1]):
        bp=i-1
        break
if(bp<0):
    print(a)
else:
    min_idx=bp+1
    for i in range(bp+1,len(a)-1):
        if(a[i]<a[min_idx] and a[i]>a[bp]):
            min_idx=i
    temp=a[min_idx]
    a[min_idx]=a[bp]
    a[bp]=temp
    i=bp+1  #reverse
    j=len(a)-1
    while(i<j):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        i=i+1
        j=j-1
print(a)



