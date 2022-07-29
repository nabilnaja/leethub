class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        for x1, x2 in equations:
            variables.add(x1)
            variables.add(x2)
        uf = UnionFind(variables)
        for i in range(len(equations)):
            uf.union(equations[i][0], equations[i][1], values[i])
            
        res = []
        for a, b in queries:
            res.append(uf.evaluate(a, b))
        
        return res
            
        
        
            
        
        
        
    
class UnionFind:
    def __init__(self, variables):
        self.rank = {var : 1 for var in variables}
        self.root = {var : var for var in variables}
        self.weight = {var : 1 for var in variables}
        
    def evaluate(self, x, y):
        
        if x not in self.weight or y not in self.weight:
            return -1.0
        r_x, w_x = self.find(x)
        r_y, w_y = self.find(y)
        
        if r_x != r_y:
            return -1.0
        
        if x == y:
            return 1
        return w_x / w_y
        
        
            
    def find(self, x):
        if self.root[x] == x:
            return x, self.weight[x]
        self.root[x], weight = self.find(self.root[x])
        self.weight[x] *= weight
        return self.root[x], self.weight[x]
        
    def union(self, x, y, value):
        r_x, w_x = self.find(x)
        r_y, w_y = self.find(y)
        if r_x != r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.root[r_y] = r_x
                self.weight[r_y] = w_x / (value * w_y)
            elif self.rank[r_y] > self.rank[r_x]:
                self.root[r_x] = r_y
                self.weight[r_x] = (w_y * value) / w_x
            else:
                self.root[r_y] = r_x
                self.rank[r_x] += 1
                self.weight[r_y] = w_x / (value * w_y)

            
        
        