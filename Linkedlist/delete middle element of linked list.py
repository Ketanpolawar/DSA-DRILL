# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: #edge cases when there is only one or none Nodes in the Linked List
#             return None
#         fast=head
#         slow=head
#         prev=None
#         while(fast is not None and fast.next is not None):
#             prev=slow
#             fast=fast.next.next
#             slow=slow.next
#         if prev:
#             prev.next=slow.next
#         return head
        
        