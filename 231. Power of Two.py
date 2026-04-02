# LeetCode 231. Power of Two
# Difficulty: Easy
# Topic: Bit Manipulation

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
