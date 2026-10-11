# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node is None:
            return

        print(node.val)
        node.left, node.right = node.right, node.left
        self.dfs(node.left)
        self.dfs(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root