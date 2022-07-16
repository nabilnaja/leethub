# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def validate(node):
            if not node:
                return True
            
            if not validate(node.left):
                return False
            nonlocal prev

            if node.val <= prev:
                return False
            prev = node.val
            return validate(node.right)
        return validate(root)
        
        
        