# # version 1

# # arr=[1,2,3,4,5,2,1,4,2,3,4]
# # map={}
# # k=3
# # ans=0
# # for i in range(len(arr)):
# #     r=k-arr[i]
# #     if r in map:
# #         ans+=map[r]
# #     if arr[i] not in map:
# #         map[arr[i]]=1
# #     else:
# #         map[arr[i]]+=1
# # print(ans)


# arr = [1, 2, 3, 4, 5, 2, 1, 4, 2, 3, 4]
# map = {}
# k = 3
# ans = 0
# pairs = []

# for i in range(len(arr)):
#     r = k - arr[i]
#     if r in map:
#         for _ in range(map[r]):
#             pairs.append((r, arr[i]))
#     if arr[i] not in map:
#         map[arr[i]] = 1
#     else:
#         map[arr[i]] += 1

# print("Number of pairs:", len(pairs))
# print("Pairs:", pairs)
