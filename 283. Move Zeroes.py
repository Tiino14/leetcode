# LeetCode 283. Move Zeroes
# Difficulty: Easy
# Topic: Two Pointers

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for n in nums:
            if n != 0:
                nums[k] = n
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
