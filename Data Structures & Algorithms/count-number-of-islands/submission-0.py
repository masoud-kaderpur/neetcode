class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        lands = 0

        def bfs(r, c):
            q = deque([(r, c)])	
            seen.add((r, c))
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]		

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))	

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    lands += 1

        return lands

