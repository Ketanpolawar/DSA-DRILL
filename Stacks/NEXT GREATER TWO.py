# from collections import deque

# class Stack:
#     def __init__(self):
#         self.container=deque()
#     def pop(self):
#         return self.container.pop()
#     def push(self,x):
#         self.container.append(x)
#     def peek(self):
#         return self.container[-1]
#     def size(self):
#         return len(self.container)
#     def isempty(self):
#         return len(self.container)==0
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         st=Stack()
#         res=[-1]*len(nums)
#         for i in range(2*len(nums)-1,-1,-1):
#             while(not st.isempty() and nums[st.peek()]<=nums[i%len(nums)]):
#                 st.pop()
#             if not st.isempty():
#                 res[i%len(nums)]=nums[st.peek()]
#             else:
#                 res[i%len(nums)]=-1
#             st.push(i%len(nums))
#         return res
            
            

        