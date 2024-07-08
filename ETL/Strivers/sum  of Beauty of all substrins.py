def beauty(s) :
    freq={}
    for i in s:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    v=list(freq.values())
    for i in range(len(v)):
        for j in range(len(v)-1-i):
            if v[j]>v[j+1]:
                v[j],v[j+1]=v[j+1],v[j]
    beauty=abs(v[0]-v[-1])
    return beauty

s='aabcb'
bsum=0
for i in range(len(s)):
    a=s[i]
    for j in range(i+1,len(s)):
        a=a+s[j]
        x=beauty(a)
        bsum=bsum+x
print(bsum)
