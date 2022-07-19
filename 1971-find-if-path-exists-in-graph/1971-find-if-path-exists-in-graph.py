class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Time complexity: O(v + e)  
        Space complexity:  O(v + e)        
        """
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination :
                return True
            if node in visited:
                continue
            visited.add(node)
            stack.extend([next_node for next_node  in graph[node]])
        return False