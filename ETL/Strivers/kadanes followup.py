#kadens followup printing the subaray

a=[1,2,3,4,5,-1,-3,8]
maxsum=-float('inf')
s=0
arrs=-1
arre=-1
end=-1
for i in range(len(a)):
    if(s==0):
        start=i #STARTING OF NEW SUBAARY IS STORED
    s=s+a[i]
    if s>maxsum:
        maxsum=s
        arrs=start
        arre=i
    if(s<0):
        s=0
if(maxsum<0):
    maxsum=0
print(a[arrs:arre+1])
