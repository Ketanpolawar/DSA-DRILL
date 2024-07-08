#rotate the  array left and right at place o(n)
a=[1,2,3,4]
k=1
def rev(a):
    i=0
    j=len(a)-1
    for i in range(len(a)//2):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j=j-1
    return a
k=k%len(a)
if(k==0):
    print(a)
else:
    a=rev(a)
    print(a)
    b=a[:k]
    print(b)
    b=rev(b)
    print(b)
    c=a[k:]
    print(c)
    c=rev(c)
    print(c)
    a[:k]=b
    a[k:]=c
print(a)

# optimal o(n)
# for bruteforce use extra array and append to the index (o(n),o(n))