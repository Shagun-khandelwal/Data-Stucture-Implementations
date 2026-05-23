# You are given an integer array nums.

# In one operation, you can choose any two distinct indices i and j and swap nums[i] and nums[j].

# Return an integer denoting the minimum number of operations required to move all 0s to the end of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]

# Output: 2

# Explanation:

# We perform the following swap operations:

# Swap nums[0] and nums[3], giving nums = [3, 1, 0, 0, 12].
# Swap nums[2] and nums[4], giving nums = [3, 1, 12, 0, 0].
# Thus, the answer is 2.

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # way 1
        count_0 = sum([1 if x==0 else 0 for x in nums])

        j = len(nums)-1
        back_count_0 = 0

        for _ in range(count_0):
            if nums[j]==0:
                back_count_0+=1
            j-=1
        return count_0 - back_count_0

        # way 2
        # i=0
        # j=len(nums)-1
        # min_operations=0
        # while i<j and nums[j]==0:
        #     j-=1
        # while i<j and nums[j]!=0:
        #     if nums[i]==0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         min_operations += 1
        #         while i<j and nums[j]==0:
        #             j-=1
        #     i+=1
        # return min_operations