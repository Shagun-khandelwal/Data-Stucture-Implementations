# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
from typing import List
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num//2 if num>4 else num
        while start<=end:
            mid = (start+end)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                end=mid-1
            else:
                start=mid+1
        return False
