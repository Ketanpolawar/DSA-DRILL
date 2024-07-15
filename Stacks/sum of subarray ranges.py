#compute the left smaller and right smaller for each indices 


def leftsmallerindices(arr):
    res=[-1]*(len(arr))
    st=[]
    for i in range(len(arr)):
        while(st and arr[st[-1]]>arr[i]):
            st.pop()
        if st:
            res[i]=st[-1]#to start from just next index which can satisfy the height
        else:
            res[i]=-1 #it means all are samller and can take part in rectangle
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

def leftgreaterindices(arr):
    res=[-1]*(len(arr))
    st=[]
    for i in range(len(arr)):
        while(st and arr[st[-1]]<=arr[i]):
            st.pop()
        if st:
            res[i]=st[-1]#to start from just next index which can satisfy the height
        else:
            res[i]=-1 #it means all are samller and can take part in rectangle
        st.append(i)
    return res


def rightgreaterIndices(arr):
    res=[-1]*(len(arr))
    st=[]
    for i in range(len(arr)-1,-1,-1):
        while(st and arr[st[-1]]<=arr[i]):
            st.pop()
        if st:
            res[i]=st[-1]
        else:
            res[i]=len(arr) #it means all are samller and can take part in rectangle
        st.append(i)
    return res



def sum_of_subarray_minimum(arr):
    ls=leftsmallerindices(arr)
    rs=rightsmallerIndices(arr)
    count=0
    for i in range(len(arr)):
        right=rs[i]-i
        left=i-ls[i]
        ans=right*left*arr[i]
        count=(count+ans)

    return count


def sum_of_subarray_maximum(arr):
    ls=leftgreaterindices(arr)
    rs=rightgreaterIndices(arr)
    count=0
    for i in range(len(arr)):
        right=rs[i]-i
        left=i-ls[i]
        ans=right*left*arr[i]
        count=(count+ans)

    return count

def sum_of_sunarrry_ranges(arr):
    return sum_of_subarray_maximum(arr)-sum_of_subarray_minimum(arr)