#O(n^2) soliution 


# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         ans = 0
#         for i in range(len(s)):
#             counter = {}
#             for j in range(i, len(s)):
#                 if s[j] in counter:
#                     counter[s[j]] += 1
#                 else:
#                     counter[s[j]] = 1
                
#                 if len(counter) == 3:
#                     ans += 1
#                 elif len(counter) > 3:
#                     break
        
#         return ans

    


#optimized approach 


# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         ans = 0
#         counter = {}
#         left = 0
        
#         for right in range(len(s)):
#             if s[right] in counter:
#                 counter[s[right]] += 1
#             else:
#                 counter[s[right]] = 1
            
#             while len(counter) == 3:
#                 ans += len(s) - right  # Every substring ending at 'right' and starting from any index in [left, right] is valid
#                 counter[s[left]] -= 1
#                 if counter[s[left]] == 0:
#                     del counter[s[left]]
#                 left += 1
        
#         return ans        