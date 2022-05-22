# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current):
            if not current:
                return False
            left = recurse_tree(current.left) 
            right = recurse_tree(current.right)
            mid = current == p or current == q
            if mid + left + right >= 2:
                self.result = current
            return left or right or mid
             
        recurse_tree(root)
        return self.result
            
       
        