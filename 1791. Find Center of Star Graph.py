# LeetCode 1791. Find Center of Star Graph
# Difficulty: Easy
# Topic: Graph

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # Center appears in both first and second edge
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
