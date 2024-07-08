s="2212"
a=''
m=-float('inf')
for i in range(len(s)-1,-1,-1):
    if(int(s[i])%2!=0):
        a=s[:i+1]
        a=int(a)
        m=max(a,m)
if m!=-float('inf'):
    print(m)
else:
    print("he he")

