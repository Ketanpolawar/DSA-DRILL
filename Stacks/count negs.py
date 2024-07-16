# class Solution:
#     def count_NGEs(self, N, arr, queries):
#         st = []
#         res = [-1] * N  # Initialize result array with -1s
     
#         # Step 1: Find Next Greater Elements using a stack
#         for i in range(N - 1, -1, -1):  # Reverse iteration from end to start
#             while st and st[-1] <= arr[i]:
#                 st.pop()
#             if st:
#                 res[i] = st[-1]
#             st.append(arr[i])
        
#         # Step 2: Calculate counts of NGEs from each index to the end
#         nge_count = [0] * N
#         for i in range(N - 2, -1, -1):#last element will be zero anyways 
#             if res[i] != -1:
#                 nge_count[i] = nge_count[i + 1] + 1
#             else:
#                 nge_count[i] = 0
        
#         # Step 3: Answer each query using precomputed nge_count
#         ans = []
#         for query in queries:
#             ans.append(nge_count[query])
        
#         return ans
