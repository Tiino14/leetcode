# LeetCode 739. Daily Temperatures
# Difficulty: Medium
# Topic: Stack (Monotonic)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  # stores indices of decreasing temperatures
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
