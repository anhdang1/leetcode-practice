# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        
        def inorder(root):
            if root is None:
                return
            #Perform inorder traversal
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res 
    
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """