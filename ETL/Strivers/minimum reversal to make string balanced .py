# # str_input = "{}{}}}{}}}"
# # st = []
# # if len(str)%2!=0:
# #     print("np")
# # for i in str_input:
# #     if i == "{":
# #         st.append(i)
# #     elif i == "}" and st and st[-1] == "{":
# #         st.pop()
# #     else:
# #         st.append(i)

# # m = 0  # Count of unmatched '{'
# # n = 0  # Count of unmatched '}'

# # for i in st:
# #     if i == '{':
# #         m += 1
# #     else:
# #         n += 1

# # print([m//2] + [n//2])



# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         balance = 0
#         moves = 0
        
#         for char in s:
#             if char == '(':
#                 balance += 1
#             else:
#                 balance -= 1
            
#             if balance < 0:
#                 moves += 1
#                 balance = 0
        
#         moves += balance
#         return moves