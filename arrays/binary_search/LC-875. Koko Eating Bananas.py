# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(banana_limit,piles,hour):
            hour_spend=0
            for ele in piles:
                hour_spend += (ele+banana_limit-1)//banana_limit
            return hour_spend <= hour
                
        start = 1
        end = max(piles)
        ans = start
        while start<= end:
            mid = (start+end)//2
            if canEat(mid,piles,h):
                end = mid-1
                ans=mid
            else:
                start=mid+1
        return ans