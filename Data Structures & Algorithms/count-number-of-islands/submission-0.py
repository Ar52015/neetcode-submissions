class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        res = 0
        visited = set()
        prev_Track = False

        h = len(grid)
        w = len(grid[0])

        def dfs(i, j):
            if i < 0 or i > h-1 or j < 0 or j > w-1 or (i, j) in visited or grid[i][j] == "0":
                return
            visited.add((i, j))
            dfs (i-1, j)
            dfs (i+1, j)
            dfs (i, j+1)
            dfs (i, j-1)
            return

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    dfs(i, j)

        return res