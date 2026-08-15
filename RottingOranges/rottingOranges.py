class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        myQueue = deque()
        minute = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    myQueue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while myQueue and fresh > 0:
            level = len(myQueue)
            minute += 1
            for _ in range(level):
                i, j = myQueue.popleft()
                for di,dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = di+i, dj+j
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        myQueue.append((ni,nj))

        if fresh != 0:
            return -1
        return minute
