class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i,j)
            
        temp = {}
        for i in range(len(s)):
            root = uf.find(i)
            if root not in temp:
                temp[root] = [[],[]]
                
            temp[root][0].append(s[i])
            temp[root][1].append(i)
        
        res = [0] * len(s)
        for text in temp.values():
            text[0].sort()
            for i , char in zip(text[1], text[0]):
                res[i] = char
        return ''.join(res)
                
            
        
                 

        
        

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = [i for i in range(n)]
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
                