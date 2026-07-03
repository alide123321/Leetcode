class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        def bfs(i,j):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] == "0" or ((i,j) in visited):
                return
            
            visited.add((i,j))

            bfs(i - 1, j)
            bfs(i + 1, j)
            bfs(i, j - 1)
            bfs(i, j + 1)

        numOfIslands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == "0":
                    continue
                if (i,j) in visited:
                    continue

                bfs(i,j)
                numOfIslands += 1

        return numOfIslands
                
                