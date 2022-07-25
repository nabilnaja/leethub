class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x : x[0])
        uf = UnionFind(n)
        for time, x, y in logs:
            uf.union(x,y)
            if uf.connected == 1:
                return time
        return -1 

class UnionFind():
    def __init__(self, n):
        self.rank = [1 for _ in range(n)]
        self.root = [i for i in range(n)]
        self.connected = n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.connected -= 1
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
                
        