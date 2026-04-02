# LeetCode 2224. Minimum Number of Operations to Convert Time
# Difficulty: Easy
# Topic: Greedy

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        diff = to_minutes(correct) - to_minutes(current)
        ops = 0
        for step in [60, 15, 5, 1]:
            ops += diff // step
            diff %= step
        return ops
