# LeetCode 658. Find K Closest Elements
# Difficulty: Medium
# Topic: Binary Search

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Binary search for left boundary of k-element window
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
