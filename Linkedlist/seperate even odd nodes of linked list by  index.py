# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         headeven=ListNode(0) #this is a dummy list to store even values with first node val is 0 
#         headodd=ListNode(0)#this is a dummy list to store odd values with odd val is 0

#         oddcurr=headodd     #this is head for oddlist points to first node
#         evencurr=headeven   # this is head for evenlist points to first node
#         curr=head# to traverse original linked list
#         is_odd=True 

#         while(curr):
#             if(is_odd):
#                 oddcurr.next=curr
#                 oddcurr=oddcurr.next
#             else:
#                 evencurr.next=curr
#                 evencurr=evencurr.next
#             curr=curr.next
#             is_odd=not is_odd
#         oddcurr.next=headeven.next
#         evencurr.next=None
#         return headodd.next


        