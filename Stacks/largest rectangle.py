#compute the left smaller and right smaller for each indices 


def leftsmallerindices(arr):
    res=[-1]*(len(arr))
    st=[]
    for i in range(len(arr)):
        while(st and arr[st[-1]]>= arr[i]):
            st.pop()
        if st:
            res[i]=st[-1]+1 #to start from just next index which can satisfy the height
        else:
            res[i]=0 #it means all are samller and can take part in rectangle
        st.append(i)
    return res
def rightsmallerIndices(arr):
    res=[-1]*(len(arr))
    st=[]
    for i in range(len(arr)-1,-1,-1):
        while(st and arr[st[-1]]>=arr[i]):
            st.pop()
        if st:
            res[i]=st[-1]
        else:
            res[i]=len(arr) #it means all are samller and can take part in rectangle
        st.append(i)
    return res
def largestrectangele(arr):
    ls=leftsmallerindices(arr)
    rs=rightsmallerIndices(arr)
    mr=0
    for i in range(len(arr)):
        area=(rs[i]-ls[i])*arr[i]
        mr=max(mr,area)
    return mr

