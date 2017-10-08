class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        x_len, y_len = len(grid), len(grid[0])

        def check_next(x, y):
            next_valid = 0
            if x - 1 >= 0 and grid[x - 1][y]:
                grid[x - 1][y] = 0
                next_valid += 1 + check_next(x - 1, y)
            if x + 1 < x_len and grid[x + 1][y]:
                grid[x + 1][y] = 0
                next_valid += 1 + check_next(x + 1, y)
            if y - 1 >= 0 and grid[x][y - 1]:
                grid[x][y - 1] = 0
                next_valid += 1 + check_next(x, y - 1)
            if y + 1 < y_len and grid[x][y + 1]:
                grid[x][y + 1] = 0
                next_valid += 1 + check_next(x, y + 1)
            return next_valid

        max_island = 0
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j]:
                    grid[i][j] = 0
                    max_island = max(1 + check_next(i, j), max_island)

        return max_island
