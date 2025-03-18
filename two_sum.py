from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, number in enumerate(nums):
            print(i, number)
            print(f"Tar:{target} - num: {number}")
            if target - number in h:
                return [i, h[target - number]]
            h[number] = i
            print(h)


# testcase = [3,2,3], target = 6
# expected = [0,2]

# [2,7,11,15] , target = 9

s = Solution()
print(s.twoSum(nums= [2,7,11,15], target=18))
