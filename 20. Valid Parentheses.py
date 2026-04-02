# LeetCode 20. Valid Parentheses
# Difficulty: Easy
# Topic: Stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mapping:
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
