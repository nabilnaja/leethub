# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')
        def helper(root):
            if not root:
                return 0
            
            right = max(helper(root.right), 0)
            left = max(helper(root.left), 0)
            nonlocal best
            best = max(best , left + right + root.val)
            return  max(left , right ) + root.val
            
        helper(root)
        return best
        