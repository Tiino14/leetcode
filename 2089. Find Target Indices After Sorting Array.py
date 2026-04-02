# LeetCode 2089. Find Target Indices After Sorting Array
# Difficulty: Easy
# Topic: Array & Sorting

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, n in enumerate(nums) if n == target]
