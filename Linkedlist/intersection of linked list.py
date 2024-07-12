# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         temp1 = headA
#         temp2 = headB
        
#         if not headA or not headB:
#             return None
        
#         # If both pointers are already pointing to the same node, return that node
#         if temp1 == temp2:
#             return temp1

#         # Traverse until intersection node is found or both reach the end
#         while temp1 != temp2:
#             temp1 = temp1.next
#             temp2 = temp2.next
            
#             # If they meet, return the intersection node
#             if temp1 == temp2:
#                 return temp1
            
#             # Reset temp1 to headB if it reaches the end of headA
#             if not temp1:
#                 temp1 = headB
            
#             # Reset temp2 to headA if it reaches the end of headB
#             if not temp2:
#                 temp2 = headA
        
#         return temp1  # Return the intersection node or None if no intersection


#approch 2 is to use hashing and check the value is traved or not 
#approch three calculate len od A and len B calculate difference move the longer one by d and then check if they collide or not