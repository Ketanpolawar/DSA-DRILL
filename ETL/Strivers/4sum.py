def sum4(arr,target):
    arr.sort()
    ans=[]
    for i in range(len(arr)):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,len(arr)):
            if j!=i+1 and arr[j]==arr[j-1]:
                continue
            k=j+1
            l=len(arr)-1
            s=arr[i]+arr[j]+arr[k]+arr[l]
            if(s==target):
                ans.append([arr[i],arr[j],arr[k],arr[l]])
                k=k+1
                l=l+1
                while(k<l and arr[k]==arr[k-1]):
                    k=k+1
                while(k<l and arr[l]==arr[l-1]):
                    l=l-1
            elif(s>target):
                l=l-1
            else:
                k=k+1
        return ans
            
            
            

