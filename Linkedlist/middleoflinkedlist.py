#by using the concept of fast and slow pointers

# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         start=head
#         end=head
#         while start and start.next:
#             start,end=start.next.next,end.next
#         return end