# 1189. Maximum Number of Balloons
# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

from typing import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        text_count = Counter(text)
        balloon_count = {'b': 1, 'a': 1, 'l': 2, 'o':2, 'n': 1}

        return min(text_count.get(char, 0) // balloon_count[char] for char in balloon_count)
            





res = Solution()
print(res.maxNumberOfBalloons(text='nlaebolko'))