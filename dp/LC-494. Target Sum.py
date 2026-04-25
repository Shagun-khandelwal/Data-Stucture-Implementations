# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
from typing import List
# since we use memoization, the time complexity is O(n * sum(nums)) because we are storing the results of subproblems in a dictionary and each subproblem is defined by the index and the current sum. The space complexity is also O(n * sum(nums)) because in the worst case, we can have n * sum(nums) unique subproblems that we need to store in the dictionary.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        def targetSum(index,curr_sum):
            # base case
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            if (index,curr_sum) in memo.keys():
                return memo[(index,curr_sum)]
            # choose +
            add = targetSum(index+1,curr_sum + nums[index])
            # choose -
            sub = targetSum(index+1,curr_sum - nums[index])
            memo[(index,curr_sum)] = add+sub
            return memo[(index,curr_sum)]
        
        return targetSum(0,0)
