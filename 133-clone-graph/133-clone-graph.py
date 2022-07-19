"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Time complexity: O(v + e)  
        Space complexity:  O(v)        
        """
        node_cache = {}
        
        def get_node(current_node):
            if not current_node:
                return None
            
            nonlocal node_cache
            
            if current_node in node_cache:
                return node_cache[current_node]
            
            node_copy = Node(current_node.val)
            node_cache[current_node] = node_copy
            
            for neighbor in current_node.neighbors:
                node_copy.neighbors.append(get_node(neighbor))
                
            
            return node_copy
        
        return get_node(node)
            
            
            
            