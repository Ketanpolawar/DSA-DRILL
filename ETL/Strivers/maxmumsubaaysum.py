#using floating window 
a=[1,2,3,4,5,6]
maxsum=0
l=0
r=0
s=0
while(l<r):
    s=s+a[r]
    r=r+1
    maxsum=max(maxsum,s)
    while(s<maxsum):
        s=s-a[l]
        l=l+1
print(maxsum)
