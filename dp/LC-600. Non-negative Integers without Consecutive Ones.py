# Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 

# Example 1:

# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
class Solution:
    def findIntegers(self, n: int) -> int:
        valid_binary = [0] * (32) # 0->31
        valid_binary[0] = 1
        valid_binary[1] = 2
        for i in range(2,32):
            valid_binary[i] = valid_binary[i-1] + valid_binary[i-2]
        
        ans = 0
        prev_bit = 0

        for i in range(30,-1,-1):
            if n & (1<<i):
                ans += valid_binary[i]
                if prev_bit == 1:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0
        return ans+1
    