# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(root, val):
            if not root: 
                return True
            if not all([helper(root.left, root.val) , helper(root.right ,root.val)]):
                return False
            self.count += 1
            return root.val == val
            
        if not root:
            return 0
        self.count = 0
        helper(root, root.val)
        return self.count
        