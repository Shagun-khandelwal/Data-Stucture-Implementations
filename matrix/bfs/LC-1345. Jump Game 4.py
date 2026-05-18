# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:

# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
# time complexity is O(N) because in the worst case, we might have to visit every index in the array to find the minimum number of steps to reach the last index. Therefore, the overall time complexity is O(N).
# space complexity is O(N) because in the worst case, we might have to store all the indices in the queue for BFS. Additionally, the visited set can also grow up to O(N) in the worst case. Therefore, the overall space complexity is O(N).
from typing import List
from collections import deque,defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return 0

        mydict=defaultdict(list)
        for idx,ele in enumerate(arr):
            mydict[ele].append(idx)

        queue=deque([0])
        visited = {0}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()

                if curr_idx == n-1:
                    return steps

                neighbours = [curr_idx-1,curr_idx+1]
                
                if arr[curr_idx] in mydict:
                    neighbours.extend(mydict[arr[curr_idx]])
                    del mydict[arr[curr_idx]] # clear to prevent O(n^2) loops
                
                for jump_idx in neighbours:
                    if  0<=jump_idx<n and jump_idx not in visited:
                        visited.add(jump_idx)
                        queue.append(jump_idx)
            steps += 1

        return steps