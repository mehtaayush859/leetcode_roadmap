# 14. Longest Common Prefix

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        print(strs)
        index_1 = strs[0]
        index_2 = strs[-1]
        i = 0

        while i<len(index_1) and i<len(index_2) and index_1[i] == index_2[i]:
            i += 1

        prefix = index_1[:i]
        if prefix == "":
            return
        return prefix


     

    

res = Solution()
print(res.longestCommonPrefix(strs = ["flower","flow","flight"]))