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
        
        def count(current, max_value= float('-inf'), previous = None):
            if not current:
                return
            nonlocal good_node_count
            
            if not previous:
                good_node_count += 1
            else:
                max_value = max(max_value, previous.val)
                if max_value <= current.val:
                    good_node_count += 1
            count(current.left, max_value, current)
            count(current.right, max_value, current)
        count(root)
        return good_node_count