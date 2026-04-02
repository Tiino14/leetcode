# LeetCode 153. Find Minimum In Rotated Sorted Array
# Difficulty: Medium
# Topic: Binary Search

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # min is in right half
            else:
                right = mid     # mid could be the min
        return nums[left]
