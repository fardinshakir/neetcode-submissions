# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, depth, depth_max):
        if node is None:
            depth_max = max(depth_max, depth)
            return depth_max

        depth += 1

        depth_max = self.dfs(node.left, depth, depth_max)

        depth_max = self.dfs(node.right, depth, depth_max)
        return depth_max

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = self.dfs(root, 0, 0)
        return max_depth