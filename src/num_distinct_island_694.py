class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        x_len, y_len = len(grid), len(grid[0])

        def check_next(x, y, i, j, cord):
            if x - 1 >= 0 and grid[x - 1][y]:
                grid[x - 1][y] = 0
                cord.append((i - 1, j))
                check_next(x - 1, y, i - 1, j, cord)
            if x + 1 < x_len and grid[x + 1][y]:
                grid[x + 1][y] = 0
                cord.append((i + 1, j))
                check_next(x + 1, y, i + 1, j, cord)
            if y - 1 >= 0 and grid[x][y - 1]:
                grid[x][y - 1] = 0
                cord.append((i, j - 1))
                check_next(x, y - 1, i, j - 1, cord)
            if y + 1 < y_len and grid[x][y + 1]:
                grid[x][y + 1] = 0
                cord.append((i, j + 1))
                check_next(x, y + 1, i, j + 1, cord)
            return cord

        distinct = dict()
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j]:
                    grid[i][j] = 0
                    island = tuple(check_next(i, j, 0, 0, [(0, 0)]))
                    distinct[island] = 1

        return len(distinct)
