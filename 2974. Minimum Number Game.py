# LeetCode 2974. Minimum Number Game
# Difficulty: Easy
# Topic: Array & Heap

import heapq

class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            # Bob appends his first, then Alice
            result.append(bob)
            result.append(alice)
        return result
