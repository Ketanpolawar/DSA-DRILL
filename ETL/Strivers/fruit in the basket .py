arr = [1, 2, 1, 2, 3, 2, 2]
k = 2
counter={}
l = 0
r=0
maxlen = 0
while(r<len(arr)):
    if(arr[r] in counter):
        counter[arr[r]]=counter[arr[r]]+1
    else:
        counter[arr[r]]=1
    while len(counter)>k:
        counter[arr[l]]-=1
        if counter[arr[l]]==0:
            del counter[arr[l]]
        l=l+1
    maxlen=max(maxlen,r-l+1)
    r+=1
    
print(maxlen)



print(maxlen)

