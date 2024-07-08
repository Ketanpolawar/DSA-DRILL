# Q1 gcd of 2 numbers

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# Q2 GCD of an array
# l = [1,2,3]
# x = l[0]
# for i in range(1, len(l)):
#     x = gcd(x, l[i])
# print(x)  # Output should be 1


# Q3 lcm of 2 numbers 
# a=10
# b=20
# lcm=a*b//gcd(a,b)
# print(lcm)



# Q4 lcm of list
# l=[1,2,8,3]
# lcm=l[0]
# for i in range(1,len(l)):
#     lcm=lcm*l[i]//gcd(lcm,l[i])
# print(lcm)


# Q5 minimum insertions to make list coprime
# l= [2,4,6]
# count=0
# for i in range(1, len(l)):
#     x = gcd(l[i],l[i-1])
#     if(x!=1):
#         count=count+1
# print(count)  



# Q6 Convert array to voprime array
# l= [2,4,6]
# print(l[0], end = " ")
# for i in range(1, len(l)):
#     x = gcd(l[i],l[i-1])
#     if(x!=1):
#         print(1, end = " ")
#     print(l[i] , end = " ")


# Q7 Minimum operations to make GCD of array a multiple of k (multiple se eak bada ya choto)

# l=[4,9,6]
# k=5
# count=0
# for i in  range(len(l)):
#     if(l[i]!=1 and l[i]>k):
#         count=count+min(l[i]%k,k-l[i]%k)
#     else:
#         count=count+1
# print(count)


# Q8 lcm of n natural number 

# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# n=10
# lcm=1
# for i in range(1,n):
#     lcm=lcm*i//gcd(lcm,i)
# print(lcm)

#Q9 Given GCD find number of possiable pairs(a,b)

# l=12
# g=2
# ans=l*g
# x=[]
# for i in range(2,l+1):
#     for j in range(2,l+1):
#         if gcd(i,j)==g:
#             if (i*j==ans):
#                 x.append((i,j))
# print(x)

#Q10 divisiable by x but not by y

# # Python 3 implementation of above approach
# from math import gcd
 
# # Function to count total numbers divisible 
# # by x but not y in range 1 to N
# def countNumbers(X, Y, N):
     
#     # Count total number divisible by X
#     divisibleByX = int(N / X)
 
#     # Count total number divisible by Y
#     divisibleByY = int(N / Y)
 
#     # Count total number divisible 
#     # by either X or Y
#     LCM = int((X * Y) / gcd(X, Y))
#     divisibleByLCM = int(N / LCM)
#     divisibleByXorY = (divisibleByX +
#                        divisibleByY -
#                        divisibleByLCM)
 
#     # Count total numbers divisible by 
#     # X but not Y
#     divisibleByXnotY = (divisibleByXorY -
#                         divisibleByY)
 
#     return divisibleByXnotY

# Gcd of strings 


