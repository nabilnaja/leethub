# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        q.append(root)
        while(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node: 
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level :
                result.append(level)
        return result
        
            
        