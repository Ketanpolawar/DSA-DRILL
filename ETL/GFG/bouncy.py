n=643
x=str(n)
i=0
j=1
inc=1
dec=1
while(j<len(x)):
    if int(x[i])>int(x[j]):
        inc=0
    i=i+1
    j=j+1
i=0
j=1
while(j<len(x)):
    if int(x[i])<=int(x[j]):
        dec=0
    i=i+1
    j=j+1
if inc==1:
    print("increasing")
elif dec==1:
    print("decreasing")
elif inc==0 and dec==0:
    print("bouncy")
