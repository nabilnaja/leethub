# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n)  
        Space complexity:  O(h)        
        """
        prev = float('-inf')
        def validate(node, left = float('-inf'), right = float('inf')):
            if not node:
                return True
            
            if not validate(node.left, left, node.val):
                return False
            
            if left >= node.val or right <= node.val:
                return False
            
            return validate(node.right, node.val, right)
        return validate(root)
        
        
        