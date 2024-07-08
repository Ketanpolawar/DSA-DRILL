#as you traverse array go on updateing the frequency of the characters
#calculate the maximum frequencies
#logic to check the the changes for current subarray will be =len ie r-l+1-maxfreq
#if the len-freq>allowed changes slide the window 
#keep on monitoring the maxlen of the array that will form


arr='AAABBCCD'
k=2
l=0
freq={}
maxlen=0
for r in range(len(arr)):
    if arr[r] in freq:
        freq[arr[r]]=freq[arr[r]]+1
    else:
        freq[arr[r]]=1
    while(r-l+1-max(freq.values())>k):
        if freq[arr[l]]==0:
            del freq[arr[l]]
        else:
            freq[arr[l]]=freq[arr[l]]-1
        l=l+1
    maxlen=max(maxlen,r-l+1)
print(maxlen)
        
