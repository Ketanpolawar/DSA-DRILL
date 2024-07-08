#compare the arrays using 2 pointer the 
# We will declare two pointers i.e. left and right. The left pointer will point to the last index of the arr1[](i.e. Basically the maximum element of the array). The right pointer will point to the first index of the arr2[](i.e. Basically the minimum element of the array).
# Now, the left pointer will move toward index 0 and the right pointer will move towards the index m-1. While moving the two pointers we will face 2 different cases like the following:
# If arr1[left] > arr2[right]: In this case, we will swap the elements and move the pointers to the next positions.
# If arr1[left] <= arr2[right]: In this case, we will stop moving the pointers as arr1[] and arr2[] are containing correct elements.


#cleverest method 
arr1=[1,2,3,0,0,0] 
arr2=[2,5,6]
for i in range(len(arr2)):
    arr1[i+len(arr2)]=arr2[i]
arr1.sort()
print(arr1)





#2bd
arr1=[2,5,6] 
arr2=[1,3,4]
i=len(arr1)-1
j=0

while(i>=0 and j<len(arr2)):
    if(arr1[i]<arr2[j]):
        break
    else:
        temp=arr1[i]
        arr1[i]=arr2[j]
        arr2[j]=temp
        i=i-1
        j=j+1
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)
    

