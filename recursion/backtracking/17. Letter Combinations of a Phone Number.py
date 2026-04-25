    # Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    # A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


    

    # Example 1:

    # Input: digits = "23"
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    # Example 2:

    # Input: digits = "2"
    # Output: ["a","b","c"]
    

    # Constraints:

    # 1 <= digits.length <= 4
    # digits[i] is a digit in the range ['2', '9'].

from typing import List
# time complexity: O(4^n * n) because in worst case we can have 4 characters for each digit and we are generating n length combinations and each combination can take O(n) time to create a string. space complexity: O(n) because we are using a temporary string to store the current combination and the maximum depth of the recursion is n.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }

        def combinations(index,sset):
            # base case
            if index == len(digits):
                res.append(sset)
                return
            
            # recursive call
            for char in phone[digits[index]]: # 4 times
                combinations(index+1,sset + char)
            

        
        res = []
        combinations(0,"")
        return res
