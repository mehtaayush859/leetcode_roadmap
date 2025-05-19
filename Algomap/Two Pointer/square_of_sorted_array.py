# 977. Squares of a Sorted Array

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j = 0,n-1
        pos = n - 1
        result = [0] * n
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[pos] = nums[i] ** 2
                i += 1
            else:
                result[pos] = nums[j] ** 2
                j -=1
            pos -= 1
        return result

        

res = Solution()
print(res.sortedSquares(nums=[-7,-3,2,3,11]))
