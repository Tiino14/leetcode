# LeetCode 2239. Find Closest Number to Zero
# Difficulty: Easy
# Topic: Array

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))
