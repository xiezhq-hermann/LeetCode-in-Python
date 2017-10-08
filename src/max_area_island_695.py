class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        x_len, y_len = len(grid), len(grid[0])

        def check_neighbor(x, y):
            if 0 <= x < x_len and 0 <= y < y_len and grid[x][y]:
                grid[x][y] = 0
                return 1 + sum([check_neighbor(x + i, y + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]])
            return 0

        max_island = 0
        for x in range(x_len):
            for y in range(y_len):
                max_island = max(check_neighbor(x, y), max_island)

        return max_island
