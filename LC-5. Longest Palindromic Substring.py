# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_odd(s,i,len_s):
            l = i-1
            r = i+1
            val = s[i]
            while (l>=0 and r < len_s):
                if s[l] == s[r]:
                    val = s[l] + val + s[r]
                else:
                    return val
                l-=1
                r+=1
            return val
        
        def check_even(s,i,len_s):
            l = i-1
            r = i
            val = ""
            while (l>=0 and r<len_s):
                if s[l] == s[r]:
                    val = s[l] + val + s[r]
                else:
                    return val
                l-=1
                r+=1
            return val
        
        len_s = len(s)
        ans = ""
        for i in range(len_s):
            if len_s == 1:
                return s
            else:
                x1 = check_odd(s,i,len_s)
                x2 = check_even(s,i,len_s)
                ans = ans if len(x1) < len(ans) else x1
                ans = ans if len(x2) < len(ans) else x2
        return ans