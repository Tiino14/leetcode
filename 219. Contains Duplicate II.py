# LeetCode 219. Contains Duplicate II
# Difficulty: Easy
# Topic: Sliding Window & Hashing

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Sliding window of size k
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
