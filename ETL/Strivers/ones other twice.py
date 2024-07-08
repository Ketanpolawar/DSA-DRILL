# xor approch 

a=[1,2,1,3,2,4,4]
ans=a[0]
for i in range(1,len(a)):
    ans= ans ^ a[i]
print(ans)