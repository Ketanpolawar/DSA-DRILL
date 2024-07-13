#Stacks in python can be implemented using 3 different ways
#1. Using list or array (if size is reached it increses size by n again)
#2. LinkedList (But the pop and push operation would require you to traverse the whole list)
#3. Use collections.deque 
#4. Optional can implement the stack class using the deque functionality as such 

from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def pop(self):
        return self.container.pop()
    def push(self,x):
        self.container.append(x)
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isempty(self):
        return len(self.container)==0
    

mystack=Stack()
mystack.push(1)
mystack.push(2)
a=mystack.pop()
mystack.push(9)
b=mystack.peek()
c=mystack.size()
d=mystack.isempty()
print(a)
print(b)
print(c,d)