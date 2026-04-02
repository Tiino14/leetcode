# LeetCode 2011. Find Smallest Index With Equal Value
# Difficulty: Easy
# Topic: Array

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1
