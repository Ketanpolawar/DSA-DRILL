# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         l = len(num)
#         i = 0
#         st = []
#         ans = ''

#         # Main loop to process the digits
#         while i < l:
#             # Remove elements from the stack if the current digit is smaller
#             # and we still have digits to remove (k > 0)
#             while k > 0 and st and st[-1] > int(num[i]):
#                 st.pop()
#                 k -= 1
#             st.append(int(num[i]))
#             i += 1
        
#         # If we still have removals left, remove from the end
#         while k > 0:
#             st.pop()
#             k -= 1
        
#         # Build the final number string from the stack
#         while st:
#             ans = str(st.pop()) + ans
        
#         # Add remaining characters from num
#         while i < len(num):
#             ans = ans + num[i]
#             i += 1
        
#         # Remove leading zeros
#         ans = ans.lstrip('0')
        
#         # Return "0" if the result is an empty string
#         return ans if ans else "0"
