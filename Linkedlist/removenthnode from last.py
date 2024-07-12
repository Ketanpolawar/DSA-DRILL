# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head:
#             return None
#         slow=head
#         fast=head
#         for i in range(n): #traverse the n steps first by fast 
#             fast=fast.next
#         if(fast is None):   #if n==len of linked liust it means we need to delete the first node of the linked list 
#             return head.next
#         while(fast.next is not None):
#             slow=slow.next
#             fast=fast.next
#         slow.next=slow.next.next
#         return head