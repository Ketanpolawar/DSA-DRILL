from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def pop(self):
        return self.container.pop()
    def push(self,x):
        if len(self.container)==0:
            self.container.append([x,x])
        elif x<=self.container[-1][1]:
            self.container.append([x,x])
        else:
            self.container.append([x,self.container[-1][1]])
    def peek(self):
        return self.container[-1][0]
    def size(self):
        return len(self.container)
    def isempty(self):
        return len(self.container)==0
    def getmin(self):
        return self.container[-1][1]
    