# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.is_balanced = True
        def dfs(root):
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) > 1:
                self.is_balanced = False
            return 1 + max(left_height, right_height)
            
        dfs(root)
        return self.is_balanced
        