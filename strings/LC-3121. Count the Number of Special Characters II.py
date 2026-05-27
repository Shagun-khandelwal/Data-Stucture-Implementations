# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

# Return the number of special letters in word.

 

# Example 1:

# Input: word = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters are 'a', 'b', and 'c'.

# Example 2:

# Input: word = "abc"

# Output: 0

# Explanation:

# There are no special characters in word.

# Example 3:

# Input: word = "AbBCab"

# Output: 0

# Explanation:

# There are no special characters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mydict = dict()
        for idx,char in enumerate(word):
            if char.lower() not in mydict:
                if 'a' <= char <= 'z': #lower
                    mydict[char] = [idx,-1]
                elif 'A' <= char <= 'Z': #upper
                    mydict[char.lower()] = [-1,idx]
            else:
                if 'a' <= char <= 'z':
                    mydict[char] = [idx,mydict[char][1]]
                else:
                    if mydict[char.lower()][1] == -1:
                        mydict[char.lower()] = [mydict[char.lower()][0],idx]
        res = 0
        for char,value in mydict.items():
            if value[0] == -1 or value[1] == -1:
                continue
            else:
                if value[0] < value[1]:
                    res += 1
        return res