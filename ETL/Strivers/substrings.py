arr=[1,2,3,4,5,6]
sunarrays=[]
for i in range (len(arr)):
    str1=[]
    for j in range(i,len(arr)):
        str1.append(arr[j])
        sunarrays.append(str1.copy())
print(sunarrays)
