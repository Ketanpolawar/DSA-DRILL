str="this is amazing"
x=str.split()
i=0
j=len(x)-1
while(i<j):
    temp=x[i]
    x[i]=x[j]
    x[j]=temp
    i=i+1
    j=j-1
s=' '.join(x)
print(s)

