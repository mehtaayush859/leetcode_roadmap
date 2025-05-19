# 242. Valid Anagram

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


from typing import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            if char not in s or freq[char] == 0:
                return False
            freq[char] -= 1
        
        return True
    
    #Simple Solution:
    # return Counter(s) == Counter(t)
    

res = Solution()
print(res.isAnagram(s = 'aaca', t ='ccac'))