# 228. Summary Ranges


# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        n = len(nums)
        res= []

        while i < n: # [0,1,2,4,5,7]
            if nums[i] + 1 == nums[i+1]:
                i += 1
            res.append(nums[:i])
            i = i
        return res

                     



res = Solution()
print(res.summaryRanges(nums = [0,1,2,4,5,7])) # ["0->2","4->5","7"]