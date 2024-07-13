# #for each index i calculate min(left heifght,right height)-current height  and sum them up to get the total answer
# #two pointers 

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l=0
#         r=len(height)-1
#         res=0
#         maxleft=0
#         maxright=0
#         while(l<=r):
#             if(height[l]<=maxright):
#                 if(height[l])>=maxleft:
#                     maxleft=height[l]
#                 else:
#                     res=res+(maxleft-height[l])
#                 l=l+1
#             else:
#                 if (height[r]>maxright):
#                     maxright=height[r]
#                 else:
#                     res=res+(maxright-height[r])
#                 r=r-1
#         return res
        