# LeetCode 2180. Count Integers With Even Digit Sum
# Difficulty: Easy
# Topic: Math & Simulation

class Solution:
    def countEven(self, num: int) -> int:
        return sum(1 for n in range(1, num + 1) if sum(int(d) for d in str(n)) % 2 == 0)
