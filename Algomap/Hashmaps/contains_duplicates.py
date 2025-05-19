# 217. Contains Duplicate

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


res = Solution()
print(res.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))