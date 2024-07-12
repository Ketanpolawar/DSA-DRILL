# #convert the linked list to array then sort the array and convert the another linkedlist 
# #optimal approach is to sort in place 

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def middle(head):
#             if not head :
#                 return None
#             slow=head
#             fast=head.next #to return first middle not the second one
#             while(fast and fast.next):
#                 fast=fast.next.next 
#                 slow=slow.next
#             return slow
#         def mergesort(head):
#             if not head or not head.next:
#                 return head
#             mid=middle(head)
#             righthead=mid.next
#             lefthead=head
#             mid.next=None #to terminate the first half
#             lefthead=mergesort(lefthead)
#             righthead=mergesort(righthead)
#             return merge(lefthead,righthead)
#         def merge(lefthead,righthead):
#             dummy=ListNode(-1)
#             start=dummy

#             while(lefthead and righthead):
#                 if(lefthead.val>= righthead.val):
#                     start.next=righthead
#                     righthead=righthead.next
#                     start=start.next
#                 else:
#                     start.next=lefthead
#                     lefthead=lefthead.next
#                     start=start.next
#             while(lefthead):
#                 start.next=lefthead
#                 start=start.next
#                 lefthead=lefthead.next
#             while(righthead):
#                 start.next=righthead
#                 righthead=righthead.next
#                 start=start.next
#             return  dummy.next
#         return mergesort(head)
            