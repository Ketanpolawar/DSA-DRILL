#class Node for current Node

class Node:
    def __init__(self,data): #init is like constructor self is like this jo bhi  Node object se call hoga
        self.data=data
        self.next=None
class LinkedList:#when ever we make any linkedlist object it will initialise its head to none
    def __init__(self):
        self.head=None
    #insert at first position or node
    def insertatfirst(self,data):
        newnode=Node(data)
        if self.head==None: #when list is empty
            self.head=newnode
        else:
            newnode.next=self.head #when list is present
            self.head=newnode
    def insertatpos(self,data,pos):
        newnode=Node(data)
        curr=self.head
        curpos=0
        prev=None
        if pos==0:#if already at that position
            newnode.next=self.head
            self.head=newnode
            return
        while(curr.next!=None and curpos<pos):#reach to that location and insert
            curpos=curpos+1
            prev=curr
            curr=curr.next
            if(curpos==pos):
                prev.next=newnode
                newnode.next=curr        
    def insertatlast(self,data):
        newnode=Node(data)
        if self.head==None: # if the list is empty
            self.head=newnode
            return
        curr=self.head
        while(curr.next!=None): #if the list is present
            curr=curr.next
        curr.next=newnode

    def printlist(self):
        curr=self.head
        while(curr.next!=None):
            print(str(curr.data)+'-->')
            curr=curr.next
        print("None")
    def deleteatfirst(self):
        if self.head==None:
            return
        else:
            self.head=self.head.next
    def deleteatlast(self):
        if self.head==None:
            return
        elif self.head.next is None:
            self.head=self.head.next
        else:
            curr=self.head
            while(curr.next!=None and curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def deleteatpos(self,pos):
        curpos=0
        curr=self.head
        if pos==0:
            if self.head==None:
                return
            else:
                self.head=self.head.next
                return
        prev=None
        while(curr.next is not None and curpos<pos):
            prev=curr
            curr=curr.next
            curpos=curpos+1
        if curr is None:
            print("position out of bounds")
            return
        prev.next=curr.next
    def findlen(self):
        if self.head is None:
            return 0
        else:
            curr=self.head
            leng=0
            while(curr.next is not None):
                leng=leng+1
                curr=curr.next
        return leng+1
    
    def findele(self,ele):
        if self.head is None:
            return None
        curr=self.head
        while(curr is not None):
            if curr.data==ele:
                return curr
            curr=curr.next
        return None
        
            

            

            


    