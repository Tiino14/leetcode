# LeetCode 2154. Keep Multiplying Found Values by Two
# Difficulty: Easy
# Topic: Array & Hashing

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
