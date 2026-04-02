# LeetCode 2078. Two Furthest Houses With Different Colors
# Difficulty: Easy
# Topic: Array & Two Pointers

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        max_dist = 0
        # Check from left end and right end
        for i in range(n):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, n - 1 - i)
            if colors[0] != colors[n - 1 - i]:
                max_dist = max(max_dist, n - 1 - i)
        return max_dist
