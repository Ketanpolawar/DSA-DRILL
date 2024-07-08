def can_jump(nums):
    max_reach = 0  # maximum index that can be reached so far
    for i in range(len(nums)):
        if i > max_reach:
            return False  # if current index i is beyond the maximum reach, return False
        max_reach = max(max_reach, i + nums[i])  # update max_reach to the furthest index that can be reached
        if max_reach >= len(nums) - 1:
            return True  # if we can reach or go beyond the last index, return True
    return False

# Example usage:
arr = [2, 3, 1, 1, 4, 0]
print(can_jump(arr))  # Output: True

arr2 = [3, 2, 1, 0, 4]
print(can_jump(arr2))  # Output: False



#Intution : keep track of farthest  index you can reach
#if current index is greater than tyhe maximim poin you can recah retuen false
#else update the max rexach
#if at any point the last index becomes reachable eturn true
