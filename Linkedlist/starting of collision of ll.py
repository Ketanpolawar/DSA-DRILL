# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         rabbit=head
#         turtle=head
#         count=0
#         while(rabbit!=None and rabbit.next!=None):
#             rabbit=rabbit.next.next
#             turtle=turtle.next
#             count=count+1
#             if(rabbit==turtle):
#                 turtle=head
#                 while(rabbit!=turtle):
#                     rabbit=rabbit.next
#                     turtle=turtle.next
#                 return turtle
#         return None
        