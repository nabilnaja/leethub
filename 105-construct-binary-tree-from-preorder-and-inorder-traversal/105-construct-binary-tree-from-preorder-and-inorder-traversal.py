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
            nonlocal pre_index
            val = preorder[pre_index]
            pre_index += 1
            in_index = inorder_map[val]
            node = TreeNode(val)
            node.left = helper(in_left, in_index - 1)
            node.right = helper(in_index + 1, in_right)
            return node
            
            
        inorder_map = { num : i for i, num in enumerate(inorder)}
        pre_index = 0

        return helper(0, len(inorder) - 1)