# LeetCode 441. Arranging Coins
# Difficulty: Easy
# Topic: Binary Search & Math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Find largest k where k*(k+1)//2 <= n
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
