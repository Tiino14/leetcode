# LeetCode 1365. How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Topic: Array & Hashing

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(n) for n in nums]
