# 344. Reverse String
# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)
res = Solution()
print(res.reverseString(s=["H","a","n","n","a","h"]))