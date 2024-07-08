# sliding window for +ve values
a=[-1,1,1]
k=1
mlength=0
s=0
if(sum(a)<k):
    print(-1)
else:
    l=0
    r=0
    while(r<len(a)):
        s=s+a[r]
        r=r+1
        while(s>k and l>r):
            s=s-a[l]
            l=l+1
        if(s==k):
            mlength=max(mlength,r-l)

print(mlength)
