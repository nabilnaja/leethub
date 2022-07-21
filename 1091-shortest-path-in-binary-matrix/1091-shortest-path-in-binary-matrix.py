class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n * m)  
        Space complexity:  O(n * m)        
        """
        start, end = (0,0,1), (len(grid) -1, len(grid[0]) -1)
        
        if not grid or not grid[0] or grid[0][0] or grid[end[0]][end[1]]:
            return -1
        moves = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        path_len = 0
        q = deque()
        q.append(start)
        while q:
            x,y,distance = q.popleft()
            if x < 0 or x>= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if (x,y) == end:
                return distance
            if grid[x][y]:
                continue
            grid[x][y] = distance
            for move_x, move_y in moves:
                q.append((x + move_x, y + move_y, distance + 1))
        return -1
                
                
        