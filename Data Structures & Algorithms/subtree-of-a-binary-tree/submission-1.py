# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, node, subRoot):

        if node is None and subRoot is None:
            return True

        if node is None or subRoot is None:
            return False

        if node.val != subRoot.val:
            return False

        return self.dfs(node.left, subRoot.left) and self.dfs(node.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.dfs(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
