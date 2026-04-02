# LeetCode 1025. Divisor Game
# Difficulty: Easy
# Topic: Math & Game Theory

class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins if and only if n is even
        return n % 2 == 0
