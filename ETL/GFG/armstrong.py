#Q1 getting armstrong numbers between the given range 
for i in range (1,1001):
    n=len(str(i))
    temp=i
    ans=0
    while(temp!=0):
        rev=temp%10
        ans=ans+rev**n
        temp=temp//10
    if(ans==i):
        print(str(i))




