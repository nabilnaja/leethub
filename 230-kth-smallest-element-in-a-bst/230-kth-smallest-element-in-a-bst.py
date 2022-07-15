# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_index = 0
        res = 0
        def find_node(node):
            if not node:
                return
            find_node(node.left)
            nonlocal current_index
            current_index += 1
            if current_index == k:
                nonlocal res
                res = node.val
                return
            find_node(node.right)
        find_node(root)
        return res
        
        