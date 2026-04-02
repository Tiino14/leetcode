# LeetCode 257. Binary Tree Paths
# Difficulty: Easy
# Topic: Trees & DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        result = []
        def dfs(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left, path + "->")
                dfs(node.right, path + "->")
        dfs(root, "")
        return result
