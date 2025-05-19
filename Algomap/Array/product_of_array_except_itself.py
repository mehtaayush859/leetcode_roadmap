# 238. Product of Array Except Self


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # i = 0
        # result = []
        # results = []
        # j = len(nums) - 1
        # while i < len(nums):
        #     if i != 0 and i < len(nums):
        #         product = result[-1] * nums[i]
        #         result.append(product)
        #     else:
        #         result.append(nums[i])
            
        #     i+=1
    
        # while j >= 0:
        #     if j != len(nums) - 1 and j >= 0:
        #         products = results[-1] * nums[j]
        #         results.append(products)
        #     else:
        #         results.append(nums[j])
    
        #     j -=1
        # return results


        n = len(nums)
        output = [1] * n
        
        # First pass: prefix (left product)
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Second pass: postfix (right product)
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output


        


res = Solution()
print(res.productExceptSelf(nums= [1,2,3,4]))