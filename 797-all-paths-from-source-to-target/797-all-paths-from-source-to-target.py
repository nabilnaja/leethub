class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O((v - 1)!)  
        Space complexity:  O(v**3)        
        """
        dest = len(graph) - 1
        visited = set()
        res = []
        current_route = []
        def dfs(current):
            if current in visited:
                return
            current_route.append(current)
            visited.add(current)
            if current == dest:
                res.append(current_route[:])
            else:
                for nei in graph[current]:
                    dfs(nei)
            visited.remove(current)
            current_route.pop()
        dfs(0)
        return res
            
                    
            
            
            
            
        