class Solution: 
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0  # Return 0 if the grid is empty

        def dfs(x: int, y: int) -> None:
            # Check for boundaries and if the cell is land
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'W':
                return
            # Mark the cell as visited
            grid[x][y] = 'W'  
            # Explore all four directions
            dfs(x + 1, y)  # Down
            dfs(x - 1, y)  # Up
            dfs(x, y + 1)  # Right
            dfs(x, y - 1)  # Left

        island_count = 0  # Initialize the count of islands

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  # Found an unvisited landmass
                    island_count += 1  # Increment island count
                    dfs(i, j)  # Visit all land connected to this one

        return island_count  # Return the total number of islands
