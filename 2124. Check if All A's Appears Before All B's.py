# LeetCode 2124. Check if All A's Appears Before All B's
# Difficulty: Easy
# Topic: String

class Solution:
    def checkString(self, s: str) -> bool:
        # 'ba' substring means a 'b' appeared before an 'a'
        return "ba" not in s
