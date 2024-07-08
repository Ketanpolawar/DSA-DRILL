#kadanes for straight array

a=[1,2,3,4,5,6,7,-1,-3]
s=0
maximum=-float('inf')
for i in range(len(a)):
    s=s+a[i]
    if(s>maximum):
        maximum=s
    if(s<0):
        s=0
if(maximum<0):
    maximum=0
print(maximum)

