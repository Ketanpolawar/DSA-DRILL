arr=[[1,2,3],[4,5,6],[7,8,9]]
left=0
right=len(arr[0])-1
top=0
bottom=len(arr)-1
while left<=right and top<=bottom:
    #    left to right
    for i in range(left,right+1):
        print(arr[top][i])
    top=top+1

    #top to bottom
    for i in range(top,bottom+1):
        print(arr[i][right])
    right=right-1


    if(top<=bottom):
        #right to left
        for i in range(right,left-1,-1):
            print(arr[bottom][i])
        bottom=bottom-1

    if left<=right:
        #bottom to top
        for i in range(bottom,top-1,-1):
            print(arr[i][left])
        left=left+1


