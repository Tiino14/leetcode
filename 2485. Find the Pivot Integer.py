# LeetCode 2485. Find the Pivot Integer
# Difficulty: Easy
# Topic: Binary Search & Math

import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # sum(1..x) == sum(x..n) => x^2 == n*(n+1)/2
        total = n * (n + 1) // 2
        x = int(math.isqrt(total))
        return x if x * x == total else -1
