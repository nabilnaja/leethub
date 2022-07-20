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
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination :
                return True
            if node in visited:
                continue
            visited.add(node)
            q.extend([next_node for next_node  in graph[node]])
        return False