# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# Example 2:

# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ln1,ln2 = len(nums1),len(nums2)
        if ln1==ln2:
            # two pointer algorithm O(N+M)
            print("two pointer")
            n,m = 0,0
            while n<ln1 and m<ln2:
                if nums1[n]==nums2[m]:
                    return nums1[n]
                elif nums1[n] > nums2[m]:
                    m+=1
                else:
                    n+=1
            return -1

        if ln1 > ln2:
            return self.getCommon(nums2,nums1)
        # ln1 should be small
        print("binary search")
        for target in nums1:
            start=0
            end = ln2-1
            while start<=end:
                mid = (start+end)//2
                if nums2[mid]==target:
                    return target
                elif nums2[mid]> target:
                    end = mid-1
                else:
                    start = mid+1
        return -1
    