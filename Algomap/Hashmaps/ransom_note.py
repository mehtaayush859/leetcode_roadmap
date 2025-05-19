# 383. Ransom Note

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count_magazine = Counter(magazine)
        for s in ransomNote:
            if s in count_magazine and count_magazine[s] > 0:
                count_magazine[s] -= 1
            else:
                return False
        return True
    

res = Solution()
print(res.canConstruct(ransomNote='aa', magazine='ab'))