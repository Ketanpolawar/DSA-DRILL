# Q1. Floating point number

# num=121.00
# s=str(num)
# j=len(s)-2
# while(j>0):
#     x=s[j+1]
#     if(s[j]=='.'):
#         if(x!='0' and int(x)%2==0):
#             print("even")
#             break
#         if(x!='0' and int(x)%2!=0):
#             print("0dd")
#             break
#         elif(x=='0' and int(s[j-1])%2!=0):
#             print("odd")
#             break
#         elif(x=='0' and int(s[j-1])%2==0):
#             print("even")
#             break


# Q2 product is even or odd 

# a=[1,2,3,4,5]
# even=0
# for i in a:
#     if i%2==0:
#         even=1
#         break
# if(even):
#     print(even)
# else:
#     print("odd")



# Q3  normal average use (A/2+B/2) 
#Q4   average without division (A+B)>>1

#  Q5 swap without 

# x=15
# y=10
# x=x+y   
# y=x-y
# x=x-y



# Q6 find trailing zeros 

# def findTrailingZeros(n):
#     if(n < 0):
#         return -1
#     count = 0
#     while(n >= 5):
#         n //= 5
#         count += n

#     return count


# # Driver program
# n = 100
# print("Count of trailing 0s " +
#       "in 100! is", findTrailingZeros(n))

# Q7 check prime or not

# n = 4
# x = int(n ** 0.5) + 1

# if n <= 1:
#     print("false")
# else:
#     for i in range(2, x):
#         if n % i == 0:
#             print("false")
#             break
#     else:
#         print("true")
   


