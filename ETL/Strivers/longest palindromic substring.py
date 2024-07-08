def ispla(s):
    return (s==s[::-1])

s="ababacfgs"
ans=-1
start=-1
end=-1
for i in range(len(s)):
    ss=s[i]
    for j in range(i+1,len(s)):
        ss=ss+s[j]
        if(ispla(ss)):
            if(len(ss)>ans):
                start=i
                end=j
                ans=len(ss)
if ans>0:
    print(ans)
    print(s[start:end+1])
else:
    print("no palindromic strings")


        





