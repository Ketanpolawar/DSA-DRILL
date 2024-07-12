# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         temp1=l1
#         temp2=l2
#         ans=ListNode(-1)
#         temp3=ans
#         carry=0
#         while(temp1 and temp2):
#             x=temp1.val+temp2.val+carry
#             temp3.next=ListNode(x%10)
#             carry=x//10
#             temp1=temp1.next
#             temp2=temp2.next
#             temp3=temp3.next
#         while(temp1):
#             x=temp1.val+carry
#             temp3.next=ListNode(x%10)
#             carry=x//10
#             temp1=temp1.next
#             temp3=temp3.next
#         while(temp2):
#             x=temp2.val+carry
#             temp3.next=ListNode(x%10)
#             carry=x//10
#             temp2=temp2.next
#             temp3=temp3.next
#         if(carry!=0):
#             temp3.next=ListNode(carry)
#         return ans.next



        