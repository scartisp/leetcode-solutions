class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        invalidCol = set()
        invalidRow = set()
        validCol = set()
        validRow = set()
        disconnected = 0
        serverCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    serverCount += 1

                    if i in invalidRow:
                        invalidRow.remove(i)
                        validRow.add(i)
                    else:
                        invalidRow.add(i)
                    
                    if j in invalidCol:
                        invalidCol.remove(j)
                        validCol.add(j)
                    else:
                        invalidCol.add(j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not(i in validRow or j in validCol):
                    disconnected += 1

        return serverCount - disconnected

