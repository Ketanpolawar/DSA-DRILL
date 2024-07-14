# from typing import List

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         st = []
#         i = 0
        
#         while i < len(asteroids):
#             if st and st[-1] > 0 and asteroids[i] < 0:
#                 collision = st[-1] + asteroids[i]
#                 if collision == 0:
#                     st.pop()
#                     i += 1
#                 elif collision < 0:
#                     st.pop()
#                 else:
#                     i += 1
#             else:
#                 st.append(asteroids[i])
#                 i += 1
        
#         return st
