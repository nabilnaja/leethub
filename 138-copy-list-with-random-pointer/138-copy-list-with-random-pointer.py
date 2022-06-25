"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n)  
        Space complexity:  O(n)        
        """
        node_clones = {}
        
        def get_clone(node):
            if not node:
                return node
            if node in node_clones:
                return node_clones[node]
            node_clone = Node(node.val)
            node_clones[node] = node_clone
            node_clone.next = get_clone(node.next)
            node_clone.random = get_clone(node.random)
            return node_clone
            
        return get_clone(head)  
            
                        
                
                
        
            
        
        
        