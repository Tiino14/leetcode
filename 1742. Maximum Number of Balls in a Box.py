# LeetCode 1742. Maximum Number of Balls in a Box
# Difficulty: Easy
# Topic: Array & Hashing

from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            boxes[sum(int(d) for d in str(i))] += 1
        return max(boxes.values())
