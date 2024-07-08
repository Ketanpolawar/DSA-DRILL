w=[10,20,30]
v=[60,100,120]
a=[]
we=50
fv=0
for i in range(len(w)):
    a.append(float(v[i]/w[i]))

for i in range(len(w)):
    minindex=i
    for j in range(i,len(w)):
        if a[j]>a[minindex]:
            minindex=j
    temp=a[i]
    a[i]=a[minindex]
    a[minindex]=temp
    temp1=w[i]
    w[i]=w[minindex]
    w[minindex]=temp1
    temp2=v[i]
    v[i]=v[minindex]
    v[minindex]=temp2     
for i in range(len(w)):
    if (we!=0):
        m=min(1,we/w[i])
        we=we-m*w[i]
        fv=fv+m*v[i]
print(fv)



