# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
# Example 2:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        length = len(bloomDay)
        if length < k*m:
            return -1

        def canMakeBouquet(Days_spent,bloomDay,bouquet_needed,flowers_in_bouquet):
            bouquet_count = 0
            consecutive_flower = 0
            for bloom in bloomDay:
                if bloom <= Days_spent:
                    consecutive_flower +=1 
                    if consecutive_flower == flowers_in_bouquet:
                        bouquet_count += 1
                        consecutive_flower = 0
                else:
                    consecutive_flower = 0
            return  bouquet_count >= bouquet_needed

        start = min(bloomDay)
        end = max(bloomDay)
        ans = start
        while start <= end:
            mid = (start+end)//2
            if canMakeBouquet(mid,bloomDay,m,k):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans