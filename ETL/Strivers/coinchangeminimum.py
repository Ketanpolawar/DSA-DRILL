coins=[1,2,5,10,20,50,100,500,1000]
j=len(coins)-1
c=0
s=0
ans=[]
k=49
for i in range(j,-1,-1):
    while(k>=coins[i]):
        k=k-coins[i]
        c=c+1
        ans.append(coins[i])
print("The minimum number of coins is", c)
print(ans)