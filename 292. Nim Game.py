# LeetCode 292. Nim Game
# Difficulty: Easy
# Topic: Math & Game Theory

class Solution:
    def canWinNim(self, n: int) -> bool:
        # Lose only if n is a multiple of 4
        return n % 4 != 0
