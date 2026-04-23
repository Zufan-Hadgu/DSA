class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()

        def valid(i,j):
            return 0 <= i< len(grid) and 0 <= j < len(grid[0])
        

        def dfs(i,j):
            if  (i,j) in visited:
                return o
            visited.add((i,j))
            perimeter = 0

            for dx,dy in direction:
                nx = i + dx
                ny = j + dy

                if not valid(nx,ny) or grid[nx][ny] == 0:
                    perimeter += 1
                elif (nx,ny) not in visited:
                    perimeter += dfs(nx,ny)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
        return 0
            

        



        