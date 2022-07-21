"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        Time complexity: O(n)  
        Space complexity:  O(n)        
        """
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            current_level = []
            for i in range(len(q)):
                node = q.popleft()
                current_level.append(node.val)
                q.extend(node.children)
            res.append(current_level)
                
        return res
                
        