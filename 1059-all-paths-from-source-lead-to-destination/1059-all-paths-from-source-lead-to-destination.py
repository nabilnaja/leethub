class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        
        for s, d in edges:
            adj[s].append(d)
        
        
        visited = set()
        processed = set()
        
        def dfs(node):
            if node in processed:
                return True
            if node in visited:
                return False
            if node == destination:
                return not adj[node]
            visited.add(node)
            neighbours = adj[node]
            if not neighbours:
                return False
            for neighbour in neighbours:
                if not dfs(neighbour):
                    return False
                else:
                    processed.add(neighbour)
            visited.remove(node)   
            return True
        return dfs(source)
            
            
            
                
            
        
        