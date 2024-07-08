class Solution:
    def frequencySort(self, s: str) -> str:
        fre={}
        for i in s:
            if i not in fre:
                fre[i]=1
            else:
                fre[i]=fre[i]+1
        val=list(fre.values())
        k=list(fre.keys())
        for i in range(len(val)-1):
            for j in range(len(val)-i-1):
                if val[j]<val[j+1]:
                    val[j], val[j+1]=val[j+1],val[j]
                    k[j],k[j+1]=k[j+1],k[j]
        s=''
        for i in range(len(val)):
            for j in range(val[i]):
                s=s+k[i]
        return s
        