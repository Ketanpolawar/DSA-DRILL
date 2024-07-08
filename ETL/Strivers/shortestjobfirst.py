class Solution:
    def solve(self, bt):
        su=0
        bt.sort()
        n=len(bt)
        wt=[0]*n
        for i in range(1,len(bt)):
            wt[i]=wt[i-1]+bt[i-1]
        y=sum(wt)
        x=y//n
        return x
        # Code here