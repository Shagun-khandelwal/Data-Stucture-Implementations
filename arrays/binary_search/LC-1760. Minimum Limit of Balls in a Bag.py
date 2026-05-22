# You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

# You can perform the following operation at most maxOperations times:

# Take any bag of balls and divide it into two new bags with a positive number of balls.
# For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
# Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

# Return the minimum possible penalty after performing the operations.

 

# Example 1:

# Input: nums = [9], maxOperations = 2
# Output: 3
# Explanation: 
# - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
# - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
# The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isCutValid(max_balls,nums,maxOperations):
        # at most max balls in every part
            operations_performed = 0
            for num in nums:
                parts = (num+max_balls-1)//max_balls
                operations_performed += (parts -1)
            return operations_performed <= maxOperations            
        
        
        ans = max(nums)
        start = 1
        end = max(nums)
        while start <= end:
            mid = (start + end )//2
            if isCutValid(mid,nums,maxOperations):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans