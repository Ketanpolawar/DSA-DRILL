a=[7,6,4,3,1]
maxprofit=0
curp=0
i=0
j=1
while(j<len(a)):
    if(a[i]<a[j]):
        curp=a[j]-a[i]
        maxprofit=max(maxprofit,curp)
        j=j+1
    elif(a[i]>a[j]):
        i=j
        j=j+1
print(maxprofit)