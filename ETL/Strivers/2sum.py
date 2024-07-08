# using dictionary complimnet approach 
a=[1,3,4,6,2,7]
k=10
s={}
for i in range(len(a)):
    compliment=k-a[i]
    if(compliment not in s):
        s[a[i]]=i
    else:
        print(i)
        print(s[compliment])

# if array is sorted optimized approach
a=[1,2,3,4,5,6,7,8]
k=10
i=0
j=len(a)-1
while(i<j):
    if(a[i]+a[j]==k):
        print(i)
        print(j)
        break
    elif(a[i]+a[j]>k):
        j=j-1
    elif(a[i]+a[j]<k):
        i=i+1