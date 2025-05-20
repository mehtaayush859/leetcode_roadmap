# 20. Valid Parentheses
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        freq = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in freq:
                if stack and stack[-1] == freq[char]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0


res = Solution()
print(res.isValid(s='([])'))
