# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums_len = len(nums)
        if nums_len < 4:
            return res
        nums.sort()
        print(nums)
        # temp = []
        # -2 -1 0 0 1 2
        for i in range(nums_len):
            for j in range(i+1,nums_len):
                k=j+1
                while k < nums_len:
                    sumi = nums[i] + nums[j] + nums[k]
                    if (target - sumi) in nums:
                        l_element = target-sumi
                        l_idx = nums.index(l_element)
                        if l_idx !=i and l_idx!=j and l_idx !=k:
                            temp_list = sorted([nums[i],nums[j],nums[k],l_element])
                            if temp_list not in res:
                                res.append(temp_list)
                # temp.append((sumi,i,j,k))
                    k+=1
        return res