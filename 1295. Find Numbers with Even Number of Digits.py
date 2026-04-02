# LeetCode 1295. Find Numbers with Even Number of Digits
# Difficulty: Easy
# Topic: Array

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)
