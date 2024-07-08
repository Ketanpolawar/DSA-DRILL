s="(***)"
c=0
for i in s:
    if(i=='('):
        c=c+1
    if(i==')'):
        c=c-1
print(c)
if(c==0):
    print("the string has valid parenthesis")
else:
    print("their is invalid")