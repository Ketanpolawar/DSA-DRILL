#use dict o(n)

s={}
se=set()
a=[1,2,8,4,2,6,8,2]
t=len(a) //3
for i in  a:
    if i not in s:
        s[i]=1
    else:
        s[i] += 1
        if s[i] > t :
            se.add(i)
print(se)
