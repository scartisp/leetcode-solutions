class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxAr = 0

        def traverse(i, j):
            if (i < 0 or j < 0) or (i >= n or j >= m) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + traverse(i,j+1) + traverse(i,j-1) + traverse(i+1,j) + traverse(i-1,j)

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxAr = max(maxAr, traverse(i,j))
        
        return maxAr
