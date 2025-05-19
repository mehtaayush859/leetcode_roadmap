# 771. Jewels and Stones


# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)

        counter = 0
        for s in stones:
            if s in jset:
                counter += 1

        return counter

res = Solution()
print(res.numJewelsInStones(jewels='aA', stones='aAAbbbb'))
