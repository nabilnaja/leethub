class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        union_find = UnionFind(n)
        
        for i in range(n):
              for j in range(i, n):
                    if i != j and isConnected[i][j]:
                        union_find.union(i,j)
        
        return union_find.provinces_number
                        
        
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.provinces_number = size
        
    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
            
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y != root_x:
            self.provinces_number -= 1
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1