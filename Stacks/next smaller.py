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
    
arr=[1,2,1]
ans=[-1]*(len(arr))
st=Stack()
for i in range(len(arr)-1,-1,-1):
    while not st.isempty() and st.peek() <= arr[i]:
        st.pop()
    if not st.isempty():
        ans[i] = st.peek()
    else:
        ans[i] = -1   
    st.push(arr[i])
print(ans)
