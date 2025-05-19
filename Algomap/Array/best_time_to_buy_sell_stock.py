# Best Time to Buy and Sell Stock

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i, j = 0, 1
        max_p = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_p = max(max_p, profit)
            else:
                i = j
            j += 1
        return max_p

res = Solution()
print(res.maxProfit(prices = [7,1,5,3,6,4]))