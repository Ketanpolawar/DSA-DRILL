# def rev(head):   #reversing the linkedlist to get add the carry easily and reverse the list back
#     prev=None
#     temp=head
#     while(temp):
#         next=temp.next
#         temp.next=prev
#         prev=temp
#         temp=next
#     return prev







# #reverse the linked list 
# head=(rev(head))
# if not head :
#     return ListNode(1)

# carry=1 #consider this to ne ythe 1 we need to add initially
# temp=head
# while temp and carry:
#     x=temp.val+carry
#     temp.val=x%10
#     carry=x//10
#     if carry and not temp.next:
#         temp.next=ListNode(carry)
#         carry=0
#     temp=temp.next
# #reverse the linked list 
# head=rev(head)
# return head
