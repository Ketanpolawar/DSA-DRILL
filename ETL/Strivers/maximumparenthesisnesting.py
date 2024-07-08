class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        maxd=0
        for i in s:
            if i=='(':
                cnt=cnt+1
                maxd=max(cnt,maxd)
            if i==')':
                cnt=cnt-1
        return(maxd)
        