# LeetCode 501. Find Mode in Binary Search Tree
# Difficulty: Easy
# Topic: Trees

from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        count = Counter()
        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_freq = max(count.values())
        return [val for val, freq in count.items() if freq == max_freq]
