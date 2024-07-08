class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        output=0
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                output+=1
                i=i+1
            j=j+1
        return output
       