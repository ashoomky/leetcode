# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_set = {}
        for i in range(len(inorder)):
            inorder_set[inorder[i]] = i
        
        # tracking index in preorder array
        self.preorder_index = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_value = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_value)
            # accessing the index of the root value in the inorder list
            mid = inorder_set[root_value]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)


