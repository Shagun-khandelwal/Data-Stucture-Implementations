# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

 

# Example 1:


# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
# Example 2:

# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# Explanation: We can use baskets 1 and 1000000000.
# time complexity is O(nlogn+ nlog(max_dist)) where n is the number of baskets and max_dist is the maximum distance between any two baskets. The sorting step takes O(nlogn) time, and the binary search step takes O(nlog(max_dist)) time because in the worst case, we might have to check all baskets for each distance in the binary search.
# space complexity is O(1) because we are using only a constant amount of extra space
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlace(position,n,total_balls,curr_distance): # O(n)
            prev_position=position[0]
            balls=1
            for i in range(1,n):
                if position[i]-prev_position >= curr_distance:
                    balls+=1
                    prev_position=position[i]
                    if balls == total_balls:
                        return True
            return False
        n=len(position)
        position.sort() #O(nlogn)
        start = 0 # minimum distance
        end = position[-1]-position[0] #max distance we can have
        ans=0
        while start<=end: #O(nlog(max_dist))
            mid=(start+end)//2
            if canPlace(position,n,m,mid):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans
