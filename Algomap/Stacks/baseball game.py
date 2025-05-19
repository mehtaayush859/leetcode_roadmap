# 682. Baseball Game

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# Example 2:

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# Example 3:

# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.


from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for i in operations:
            if i == 'C':
                result.pop()
            elif i == 'D':
                product = result[-1] * 2
                result.append(product)
            elif i == '+':
                add = result[-1] + result[-2]
                result.append(add)
            else:
                result.append(int(i))
            
        return sum(result)

res = Solution()
print(res.calPoints(operations=["1","C"]))