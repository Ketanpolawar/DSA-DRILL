
# class Solution:       IN LEFT 
#     def prevSmaller(self, A):
#         st = []
#         ans = [-1] * len(A)
#         for i in range(len(A)):
#             while st and st[-1] >= A[i]:
#                 st.pop()
#             if st:
#                 ans[i] = st[-1]
#             else:
#                 ans[i] = -1
#             st.append(A[i])
#         return ans



# class Solution:  IN RIGHT
#     def nextSmaller(self, A):
#         stack = []
#         result = [-1] * len(A)
        
#         for i in range(len(A) - 1, -1, -1):
#             while stack and stack[-1] >= A[i]:
#                 stack.pop()
#             if stack:
#                 result[i] = stack[-1]
#             stack.append(A[i])
        
#         return result
