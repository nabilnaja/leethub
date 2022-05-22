# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = preorder.pop(0)
            in_index = index_map[val]
            node = TreeNode(val)
            node.left = helper(in_left,in_index - 1)
            node.right = helper(in_index + 1,in_right)
            return node
            
        index_map = {val:index for index, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
        