# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # using DFS
        def dfs(index):
            if 0>index or index >= length or arr[index] ==-1:
                return False
            if arr[index] == 0:
                return True
            jumps = arr[index]
            arr[index]=-1
            return dfs(index+jumps) or dfs(index-jumps)
        length = len(arr)
        return dfs(start)


        # Using BFS (time -> O(N),space-> O(N))
        # if arr[start] == 0:
        #     return True
        # queue = deque([start])
        # length = len(arr)
        # while queue:
        #     popped_idx = queue.popleft()
        #     popped_value = arr[popped_idx]
        #     arr[popped_idx] =  -1 # visited
        #     for idx in (popped_idx - popped_value,popped_idx + popped_value):
        #         if 0<= idx < length and arr[idx] != -1: # idx in bound and not visited
        #             if arr[idx]==0:
        #                 return True
        #             queue.append(idx)
        # return False


