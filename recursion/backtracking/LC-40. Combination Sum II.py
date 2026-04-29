# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start,curr_list,curr_sum):
            # base case
            if curr_sum == target:
                res.append(curr_list[:])
                return

            # recursive case
            if curr_sum > target:
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                backtrack(i+1,curr_list+[candidates[i]],curr_sum+candidates[i])

        
        res=[]
        candidates.sort()
        backtrack(0,[],0)
        return res