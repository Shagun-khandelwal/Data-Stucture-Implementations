#  Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # def perm(curr,used):
        #     # base case
        #     if len(curr) == len(nums):
        #         res.append(list(curr))
        #         return
            
        #     # recursive case
        #     for i in range(len(nums)):
        #         # if we already use current element
        #         if used[i]:
        #             continue

        #         # if we didn't use current element            
        #         used[i] = True
        #         curr.append(nums[i])
        #         perm(curr,used)

        #         # backtracking
        #         used[i] =  False
        #         curr.pop()
        
        
        # res=[]
        # perm([],[False]* len(nums))
        # return res

        # by swapping
        def perm(i):
            if i == len(nums):
                res.append(list(nums))
                return
            
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]

                perm(i+1)

                nums[i],nums[j] = nums[j],nums[i]
        res=[]
        perm(0)
        return res
