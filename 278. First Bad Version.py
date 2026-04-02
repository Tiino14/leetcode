# LeetCode 278. First Bad Version
# Difficulty: Easy
# Topic: Binary Search

# def isBadVersion(version: int) -> bool: (provided by API)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid      # mid could be the first bad
            else:
                left = mid + 1   # first bad is after mid
        return left
