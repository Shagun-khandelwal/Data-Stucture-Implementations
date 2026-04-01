# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.
class Solution:
    def myAtoi(self, s: str) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
        res=""
        pos_sign=True
        sign_visit=False
        lead_space_removed=False
        skip_lead_zero=False
        lead_zero_count=0
        i=0
        while i<len(s) and s[i] not in alphabets:
            char = s[i]
            # char is space and we didn't removed all leading spaces
            if char == ' ' and (lead_space_removed == False):
                i+=1
                continue
            elif char == ' ' and (lead_space_removed == True):
                break
            # char in sign +/- and till now we haven't visit sign
            elif char in ['+','-'] and (sign_visit == False):
                if char == '-':
                    pos_sign=False
                sign_visit = True
                if not lead_space_removed:
                    lead_space_removed = True
            elif char in ["+","-"] and (sign_visit == True):
                break
            elif char == '0' and skip_lead_zero == False:
                lead_zero_count += 1
                sign_visit = True
                if not lead_space_removed:
                    lead_space_removed = True
                i+=1
                continue
            elif char in "0123456789":
                sign_visit = True
                lead_space_removed = True
                res+=char
                if not skip_lead_zero:
                    skip_lead_zero = True
            i+=1
        res = (int(res) if pos_sign==True else int(res)*-1) if len(res)>0 else 0
        if res < -1<<31:
            res = -1<<31
        if res >= 1<<31:
            res = (1<<31) -1
        return res