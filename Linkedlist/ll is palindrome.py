# #one way is to traverse the linkedlist and reverse and check then 
# #use or list and rev the list and check if it is palindrome

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return True
#         slow=head
#         fast=head
#         prev=None
#         #reverse the first half of the linked list till middle 
#         while(fast is not None and fast.next is not None):
#             fast=fast.next.next
#             Nextgo=slow.next
#             slow.next=prev
#             prev=slow
#             slow=Nextgo
            
#         if fast: #to handle odd case
#             slow=slow.next
#         while(slow!=None):
#             if(prev.val!=slow.val):
#                 return False
#             prev=prev.next
#             slow=slow.next
#         return True


