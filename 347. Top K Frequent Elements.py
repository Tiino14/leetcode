from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)