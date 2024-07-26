# #Approach 1 is to take the product of the total arry 
# #then at every index divide the product by the value

# #approah 2 without using division
# #take product of the elemnts in right and product of the elemnt in left and multiply them 


# arr=[3,4,6,1,2]
# left=[1]*len(arr)
# right=[1]*len(arr)
# for i in range(1,len(arr)):
#     left[i]=left[i-1]*arr[i-1]
# for i in range(len(arr)-2,-1,-1):
#     right[i]=right[i+1]*arr[i+1]
# for i in range(len(arr)):
#     arr[i]=left[i]*right[i]
# print(arr)