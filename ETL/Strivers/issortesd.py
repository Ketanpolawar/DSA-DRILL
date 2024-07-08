#single pass solution 2 pointers to chesk one way(eithe asc or desc) 2 pass for both


a=[5,4,6,7]
i=0
j=1
flagasc=1
flagdesc=1
while(j<len(a)):
    if(a[i]>a[j]):
        flagasc=0
        break
    i=i+1
    j=j+1
i=0
j=1
while(j<len(a)):
    if(a[i]<a[j]):
        flagdesc=0
        break
    i=i+1
    j=j+1
if(flagasc==1 or flagdesc==1):
    print("sorted")
else:
    print("notsorted")

# here we used 2 passes to check both the desc and asc for only one check one pass is required
# complexity O(N)
    