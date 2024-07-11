class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        i=0
        j=len(a)-1
        while(i<j):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i=i+1
            j=j-1
        s=' '.join(a)
        return s
    



            
        

        # or

class Solution:
    def reverseWords(self, s: str) -> str:
        count=0
        a=[]
        for i in range(0,len(s)-1):
            if(s[i].isspace()==False):
                break
            else:
                count=count+1
        print(count)
        ch=""
        for i in range(count,len(s)):
            if(s[i].isspace()):
                if ch:
                    a.append(ch)
                ch=""
            else:
                ch=ch+s[i]
        if ch:
            a.append(ch)
        ans=""
        reversed_words = ' '.join(a[::-1])
        return reversed_words
            
        