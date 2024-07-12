# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         headeven=ListNode(0)
#         headodd=ListNode(0)

#         if  not head:
#             return 
#         temp1=headeven
#         temp2=headodd
#         temp=head
#         while(temp):
#             if(temp.val %2==0):
#                 newnode=ListNode(temp.val)
#                 if not headeven:
#                     headeven=newnode
#                 else:
#                     temp1.next=newnode
#                     temp1=temp1.next
#             elif(temp.val %2 !=0):
#                 newnode=ListNode(temp.val)
#                 if not headodd:
#                     headodd=newnode
#                 else:
#                     temp2.next=newnode
#                     temp2=temp2.next
#             temp=temp.next
#         temp1.next=headodd.next
#         return headeven.next
        