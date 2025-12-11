# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

       

        def dfs(node, max_node):
            if not node:
                return 0
            
            if node.val >= max_node:
                count = 1
            else:
                count = 0
        
            max_node = max(max_node, node.val)
            count += dfs(node.left, max_node)
            count += dfs(node.right, max_node)
            return count
        
        return dfs(root, root.val)

        