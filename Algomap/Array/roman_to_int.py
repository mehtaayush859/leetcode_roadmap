# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0

        while i < len(s):
            if i < (len(s)-1) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                calc = roman_to_int[s[i+1]] - roman_to_int[s[i]]
                total += calc
                i += 2
            else:
                total += roman_to_int[s[i]]
                i += 1
        return total


res = Solution()
print(res.romanToInt(s='MCMXCIV'))