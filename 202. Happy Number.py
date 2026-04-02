# LeetCode 202. Happy Number
# Difficulty: Easy
# Topic: Math & Hashing

class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            return sum(int(d) ** 2 for d in str(num))
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = digit_square_sum(n)
        return True
