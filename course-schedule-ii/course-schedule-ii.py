class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = {}
        
        for pre, course in prerequisites:
            indegree[pre] = indegree.get(pre, 0) + 1
            adj[course].append(pre)
         
        
        q = deque([v for v in range(numCourses) if v not in indegree])
        res = []
        while q:
            v = q.popleft()
            res.append(v)
            if v in adj:
                for nei in adj[v]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        return res if len(res) == numCourses else []
            
                
                