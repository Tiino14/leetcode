# LeetCode 136. Single Number
# Difficulty: Easy
# Topic: Bit Manipulation

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result ^= n  # XOR cancels pairs, leaves single
        return result
