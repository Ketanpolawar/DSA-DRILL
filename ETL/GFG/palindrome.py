# # Q1 palindrome of integer 
# def palindrome(n):
#     temp=n
#     rev=0
#     while(temp!=0):
#         x=temp%10
#         rev=rev*10+x
#         temp=temp//10
#     print(rev)
#     if(n==rev):
#         return True
#     else:
#         return False
        
# palindrome(121)

# #Q2 palindrome of decimal number 
# def plaindrome(n):
#     a=''
#     b=''
#     c=0
#     x=str(n)
#     for i in x:
#         if i=='.':
#             break
#         else:
#             c=c+1
#             a=a+i
#     for i in range(c+1,len(x)):
#         b=b+x[i]
#     temp=int(b)
#     c=0
#     while(temp!=0):
#         v=temp%10
#         c=c*10+v
#         temp=temp//10
#     if(int(a)==int(c)):
#         print("palindrome")
# plaindrome(1332.2331)
# OR
# n=1211.121
# x=str(n)
# i=0
# j=len(x)-1
# while(i<=j):
#     if(x[i]!=x[j]):
#         ans=False
#         break
#     else:
#         ans=True
#     i=i+1
#     j=j-1
# if(ans):
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Q3 Sentence Palindrome

# sen="Too oot"
# x=sen.lower()
# i=0
# j=len(sen)-1
# while(i<=j):
#     if(not(x[i]>='a' and x[i]<='z')):
#         i=i+1
#     if(not(x[j]>='a' and x[j]<='z')):
#         j=j-1
#     if(x[i]!=x[j]):
#         ans=False
#         break
#     else:
#         ans= True
#     i=i+1
#     j=j-1
# if(ans):
#     print("Palindrome")
# else:
#     print("not palindrome")

        
# Q4 check if we can make palindrome using all char of word 

# x='malayalam'
# oddcount=0
# count={}
# for i in x:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
# for i in count:
#     if count[i]%2!=0:
#         oddcount+=1
# if(oddcount>1):
#     print("no plandrome possialbe")
# else:
#   print("palindrome possialbe")


# Q5 Lexicographically first palindrome

# x='malayalam'
# left=''
# right=''
# odd=""
# oddcount=0
# count={}
# for i in x:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
# for i in count:
#     if count[i]%2!=0:
#         odd=odd+i
#         oddcount+=1
# if(oddcount>1):
#     print("no plandrome possialbe")
# else:
#     for i in sorted(count.keys()):
#         x=count[i]
#         if(x%2==0):
#             while(x!=0):
#                 left+=i
#                 x-=1
#                 right+=i
#                 x-=1
# right=right[::-1]
# ans=left+odd+right
# print(ans)


#Q6 Sum of first k even length palindrome numbers 
# def palindrome(n):
#     temp=n
#     rev=0
#     while (temp!=0):
#         x = temp%10
#         rev=rev*10+x
#         temp=temp//10
#     if(n==rev):
#         return True
#     else:
#         return False

# k=3
# i=0
# sum=0

# while(k!=0):
#     n=len(str(i))
#     if(n%2==0):
#         if(palindrome(i)):
#             sum=sum+i
#             k-=1
#     i+=1
# print(sum)


# Q7 Palindrom in given range
# def palindrome(n):
#     temp=n
#     rev=0
#     while (temp!=0):
#         x = temp%10
#         rev=rev*10+x
#         temp=temp//10
#     if(n==rev):
#         return True
#     else:
#         return False

# for i in range(100):

#     if(palindrome(i)):
#         print(i)


# Q8 remove a element to make a plandrome number  abcdcaba
# def can_form_palindrome(s):
#     i = 0
#     j = len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             if s[i+1:j+1] == s[i+1:j+1][::-1]:
#                 return s[i], i
#             elif s[i:j] == s[i:j][::-1]:
#                 return s[j], j
#             else:
#                 return None, None
#         i += 1
#         j -= 1
#     return None, None

# x = "abcdba"
# char_to_remove, index = can_form_palindrome(x)

# if char_to_remove is not None:
#     print(f"Remove character '{char_to_remove}' at index {index} to form a palindrome.")
# else:
#     print("The string is already a palindrome or cannot be made into one by removing one character.")


# Q9 Smallest Palindrome after replacement
# x='ab..e.c.a'
# x=list(x)
# i=0
# j=len(x)-1
# while(i<j):
#     if(x[i]!='.' and x[j]=='.'):
#         x[j]=x[i]
#         i=i+1
#         j=j-1
#     elif(x[i]=='.' and x[j]!='.'):
#         x[i]=x[j]
#         i=i+1
#         j=j-1
#     elif(x[i]=='.' and x[j]=='.'):
#         x[j]='a'
#         x[i]='a'
#         i=i+1
#         j=j-1
#     else:
#         i=i+1
#         j=j-1
# x=''.join(x) 
# print(x)


# Q10 Longest plandome word in sentence
# txt="Madam Arora teaches Malayalam"
# txt=txt.lower()
# x=txt.split()
# print(x)
# m=0
# for i in range(len(x)):
#     if(x[i]==x[i][::-1]):
#         m=max(m,len(str(i)))
#         if(m==len(str(i))):
#             ans=x[i]
# print(ans)


# Q11 count palindrome in sentences
# txt="Madam Arora teaches Malayalam"
# txt=txt.lower()
# x=txt.split()
# print(x)
# m=0
# for i in range(len(x)):
#     if(x[i]==x[i][::-1]):
#         m+=m
# print(m)


# Q12 Longest Non-palindromic substring

# x='abba'
# flag=1
# for i in range(len(x)):
#     if (x[i]!=x[0]):
#         flag=0
        
# if(flag):
#     print(0)
# else:
#     if(x==x[::-1]):
#         print(len(x)-1)

# Q13 Reverse digits of number by k 

# k=-2
# num=12345
# k=k%len(str(num))
# def rev(num):
#     x=num
#     ans=0
#     while(x!=0):
#         a=x%10
#         ans=ans*10+a
#         x=x//10
#     return ans

# step1=rev(num)    
# step1=str(step1)
# if k==0:
#     ans=step1
# else:
#     step2=step1[:k]   
#     step3=rev(int(step2))
#     step4=step1[k:]
#     step5=rev(int(step4))
#     ans=str(step3)+str(step5)
# print(ans)


