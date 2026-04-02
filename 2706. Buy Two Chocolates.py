# LeetCode 2706. Buy Two Chocolates
# Difficulty: Easy
# Topic: Greedy & Sorting

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        cost = prices[0] + prices[1]
        return money - cost if cost <= money else money
