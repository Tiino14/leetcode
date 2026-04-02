# LeetCode 342. Power of Four
# Difficulty: Easy
# Topic: Bit Manipulation

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Must be power of 2 AND bit set at even position (n % 3 == 1)
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
