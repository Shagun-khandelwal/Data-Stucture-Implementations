# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
# time complexity: O(2^n * n) because in worst case we can have 2^n subsets and each subset can take O(n) time to create a list. space complexity: O(n) because we are using a temporary list to store the current subset and the maximum depth of the recursion is n.
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(index,curr):
            # base case
            if index == len(nums):
                res.append(curr[:])
                return
            # recursive case
            backtrack(index+1,curr+[nums[index]])
                # exclude it
            next_index = index
            while next_index + 1 <len(nums) and nums[next_index] == nums[next_index+1]:
                next_index+=1

            backtrack(next_index+1,curr)

        
        
        res =[]
        backtrack(0,[])
        return res
