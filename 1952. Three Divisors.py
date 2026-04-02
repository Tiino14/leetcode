# LeetCode 1952. Three Divisors
# Difficulty: Easy
# Topic: Math

class Solution:
    def isThree(self, n: int) -> bool:
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        return len(divisors) == 3
