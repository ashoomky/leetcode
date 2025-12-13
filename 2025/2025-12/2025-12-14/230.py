# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.minimum = 0
        self.count = k

        def dfs(node):
            if not node:
                return 0
            
            dfs(node.left)
            self.count -= 1
            if self.count == 0:
                self.minimum = node.val
                return
            dfs(node.right)
            
        
        dfs(root)
        return self.minimum
            
