strs=["flower","flow","flight"]
x=strs[0]
i=0
prefix=""
for j in range(len(x)):
    ch=x[j]
    for i in range(1,len(x)):
        if j>=len(strs[i]) or strs[i][j]!=ch:
            print(prefix)
            break
    prefix=prefix+ch
print(prefix)
