# def febo(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return febo(n-1) + febo(n-2)

# m = 10
# for i in range(m):
#     print(febo(i))



# # def fibonacci(n):
     
# #     i = 0
# #     l = [0,1] 
# #     while i < n-2:
# #         l.append(l[-1]+l[-2])
# #         i+=1
# #     return l
 



 

# #Creating a Fibonacci function
# def fibonacci(n):
   
#       #defining first two variables
#     a,b = 0,1
#     yield 0
#     yield 1
#     for i in range(2, n):
#         yield a+b
#         #swaping a with b and b with sum
#         a,b = b, a+b
 