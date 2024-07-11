# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         rabbit=head
#         turtle=head
#         while(rabbit!=None and rabbit.next!=None):
#             rabbit=rabbit.next.next
#             turtle=turtle.next
#             if(rabbit==turtle):
#                 turtle=turtle.next
#                 count=1
#                 while(turtle!=rabbit):
#                     turtle=turtle.next
#                     count=count+1
#                 return count
#         return 0
        