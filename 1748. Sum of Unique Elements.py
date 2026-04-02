# LeetCode 1748. Sum of Unique Elements
# Difficulty: Easy
# Topic: Array & Hashing

from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count = Counter(nums)
        return sum(n for n, c in count.items() if c == 1)
