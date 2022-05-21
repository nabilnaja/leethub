# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        """"
        q = deque([root])
        while(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            if level :
                result.append(level)
        return result
        """
        def dp(root, level, result):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                dp(root.left, level + 1, result)
            if root.right:
                dp(root.right, level + 1, result)
        dp(root,0,result)
        return result
                
            
        
            
        