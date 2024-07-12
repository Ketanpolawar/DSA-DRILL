# zero=listnode(-1)
# one=Listnode(-1)
# two=Listnode(-1)

# if not head  or not head.next:
#     return head
# zerocurr=zero
# onecurr=one
# twocurr=two

# temp=head

# while(temp):
#     if(temp.val==0):
#         zerocurr.next=temp
#         zerocurr=zerocurr.next
#     elif(temp.val==1):
#         onecurr.next=temp
#         onecurr=onecurr.next
#     elif(temp.val==2):
#         twocurr.next=temp
#         twocurr=twocurr.next
#     temp=temp.next

# if (onecurr.next):
#     zerocurr.next=one.next
# else:
#     zerocurr.next=two.next
# onecurr.next=two.next
# two.next=None


# return zero.next