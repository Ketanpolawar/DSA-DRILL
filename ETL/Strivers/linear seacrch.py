#only one way traverse the whole array and check 
a=[1,2,3,4,5,6,7,8]
k=1
flag=0
idx=-1
for i in range(len(a)):
    if(a[i]==k):
        flag=1
        idx=i
        break
if(flag):
    print("found at:" + str(idx))
else:
    print("notfound")
