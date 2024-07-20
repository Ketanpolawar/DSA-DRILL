#approch 1:sort both list and compare both list
#use map to store count compare both map
#use frequency array update on first pass ,decrese on 2nd


str1="CAT"
str2="APT"
a={}

for i in str1:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
for i in str2:
    if i in a:
        a[i]=a[i]-1
    else:
        print("not anagram")
        break
flag=0
for i in a:
    if a[i]!=0:
        print("not anagram")
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("anagram")