#sliding window 
k=10
a=[1,4,2,5,7,3,7]
s=0
l=0
r=0
count=0
while(r<len(a)):
    s=s+a[r]
    r=r+1
    while(s>k and l<=r):
        s=s-a[l]
        l=l+1
    if(s==k):
        count=count+1
        print(str(l)+" "+str(r))
print(count)