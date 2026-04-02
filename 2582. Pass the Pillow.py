# LeetCode 2582. Pass the Pillow
# Difficulty: Easy
# Topic: Greedy & Math

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Full back-and-forth cycle length is 2*(n-1)
        cycle = time % (2 * (n - 1))
        if cycle < n:
            return cycle + 1
        else:
            return 2 * n - 1 - cycle
