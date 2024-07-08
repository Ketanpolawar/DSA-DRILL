#User function Template for python3

class Solution:
    
    def atMost(self,s,k):
        if k<0:
            return 0
        
        i=0
        j=0
        res=0
        cnt=0
        m=[0 for i in range(26)]
        
        while i<len(s):
            m[ord(s[i])-ord("a")]+=1
            if m[ord(s[i])-ord("a")]==1:
                cnt+=1
            
            while cnt>k:
                m[ord(s[j])-ord("a")]-=1
                if m[ord(s[j])-ord("a")]==0:
                    cnt-=1
                
                j+=1
            
            
            res+=i-j+1
            i+=1
        
        return res

        