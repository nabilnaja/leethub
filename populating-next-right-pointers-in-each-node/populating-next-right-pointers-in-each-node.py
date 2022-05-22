"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        left_node = root
        
        while left_node.left:
            node = left_node
            while node:
                node.left.next = node.right
                
                if node.next:
                    node.right.next = node.next.left
                
                node = node.next
            left_node = left_node.left
            
        return root