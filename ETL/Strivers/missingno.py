#summation approach excellamt one 
n=10
sum1=0
sum2=0
a=[1,2,3,5,6,7,8,9,10]
for i in range(1,n+1):
    sum1=sum1+i
for i in a:
    sum2=sum2+i
ans=sum1-sum2
print(ans)

# complexity o(n)


# best approach is xor approch
# take xor of all number in array
# take xor of all numers in rabge 1 to n
# ans is xor1 xor xor 2