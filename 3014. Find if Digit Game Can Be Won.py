# LeetCode 3014. Find if Digit Game Can Be Won
# Difficulty: Easy
# Topic: Greedy & Math

class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        # Alice picks single-digit (<10), Bob picks two-digit (>=10)
        single = sum(n for n in nums if n < 10)
        double = sum(n for n in nums if n >= 10)
        return single != double
