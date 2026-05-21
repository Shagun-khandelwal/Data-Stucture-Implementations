# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def largestSumSubarray(ArraySum,subArraySum,nums,k):
            # if subArraySum can be achieved by partition our array into k parts
            part = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > subArraySum:
                    print(num,subArraySum)
                    part+=1
                    current_sum = 0
                current_sum += num
            return part <= k       
        
        total_sum = sum(nums)
        print(total_sum)
        start = max(nums)
        end = total_sum
        ans = start
        while start <= end:
            mid = (start + end)//2
            if largestSumSubarray(total_sum,mid,nums,k):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans