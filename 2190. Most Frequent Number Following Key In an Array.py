# LeetCode 2190. Most Frequent Number Following Key In an Array
# Difficulty: Easy
# Topic: Array & Hashing

from collections import Counter

class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        count = Counter(nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key)
        return count.most_common(1)[0][0]
