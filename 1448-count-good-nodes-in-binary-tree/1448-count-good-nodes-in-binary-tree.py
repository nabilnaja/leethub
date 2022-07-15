# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)  
        Space complexity:  O(n)        
        """
        good_node_count = 0
        
        def count(current, max_value= float('-inf')):
            if not current:
                return
            nonlocal good_node_count
            
            if current.val >= max_value:
                good_node_count += 1
            current_max = max(current.val, max_value)
            count(current.left, current_max)
            count(current.right, current_max)
        count(root)
        return good_node_count