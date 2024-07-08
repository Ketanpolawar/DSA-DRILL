a=[1,9,4,5,3,0,2]
s=set(a)  #can check if elemen is present in o(1) time
ans=0
for i in a:
    if(i-1 not in s):#to ensure it is starting of the subsequence
        cur_num=i
        cur_cnt=1
        while(cur_num+1 in s):#to check length of new subsequence
            cur_num+=1
            cur_cnt+=1
        ans=max(ans,cur_cnt)
print(ans)