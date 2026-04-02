# LeetCode 653. Two Sum IV - Input is a BST
# Difficulty: Easy
# Topic: Trees & Hashing

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if k - node.val in seen:
                return True
            seen.add(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return False
