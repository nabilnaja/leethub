class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1
        count = {0: 0, 1: 0, 2: 0}
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count[grid[i][j]] += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        if count[2] == 0:
            return -1 if count[1] else 0
        elif not count[1]:
            return 0
        
        days = 0
        while q:
            days += 1
            for i in range(len(q)):
                x, y = q.pop()
                for move_x, move_y in moves:
                    new_x = x + move_x
                    new_y = y + move_y
                    if new_x < 0 or new_x > m or new_y < 0 or new_y > n or not grid[new_x][new_y]:
                        continue
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.appendleft((new_x, new_y))
                        count[1] -= 1
                        if not count[1]:
                            return days
        return -1 if count[1] else days
            
        
        
        
            