# LeetCode 2215. Find the Difference of Two Arrays
# Difficulty: Easy
# Topic: Array & Hashing

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
