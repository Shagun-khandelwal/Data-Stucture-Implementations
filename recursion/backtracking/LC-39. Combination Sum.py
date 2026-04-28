# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# time complexity: O(2^n * n) because in worst case we can have 2^n combinations and each combination can take O(n) time to create a list. space complexity: O(target/(smallest candidate)) because in worst case we can have target/(smallest candidate) numbers in a combination and the maximum depth of the recursion is target/(smallest candidate).
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx,total,curr):
            # base case
            if total == target:
                res.append(curr[:])
                return
            
            if idx>=len(candidates) or total > target:
                return
            
            total += candidates[idx]
            backtrack(idx,total,curr+[candidates[idx]])
            
            total -= candidates[idx]
            backtrack(idx+1,total,curr)
            
                

        
        res=[]
        backtrack(0,0,[])
        return res