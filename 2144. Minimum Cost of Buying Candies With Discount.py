# LeetCode 2144. Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Topic: Array & Greedy

class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # Sort descending; every 3rd candy (index 2, 5, 8...) is free
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if (i + 1) % 3 != 0)
