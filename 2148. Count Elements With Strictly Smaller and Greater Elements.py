# LeetCode 2148. Count Elements With Strictly Smaller and Greater Elements
# Difficulty: Easy
# Topic: Array & Sorting

class Solution:
    def countElements(self, nums: list[int]) -> int:
        lo, hi = min(nums), max(nums)
        return sum(1 for n in nums if lo < n < hi)
