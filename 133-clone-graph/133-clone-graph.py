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
        Time complexity: O(e + v)  
        Space complexity:  O(v)        
        """
        if not node:
            return node
        node_cache = {}
        
        def get_node(current_node):
            nonlocal node_cache
            if current_node in node_cache:
                return node_cache[current_node]
            else:
                node_copy = Node(current_node.val)
                node_cache[current_node] = node_copy
                return node_copy
        visited = set()
        stack = [node]
        while stack:
            current_node = stack.pop()
            if current_node in visited:
                continue
            visited.add(current_node)
            copy_node = get_node(current_node)
            for neighbor in current_node.neighbors:
                stack.append(neighbor)
                copy_node.neighbors.append(get_node(neighbor))
        return node_cache[node]
            
            
            
            