# LeetCode 2558. Take Gifts From the Richest Pile
# Difficulty: Easy
# Topic: Array & Heap

import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Max-heap via negation
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(largest))
        return -sum(heap)
