class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        x_len, y_len = len(grid), len(grid[0])

        def check_neighbor(x, y, i, j, coordinates):
            if 0 <= x < x_len and 0 <= y < y_len and grid[x][y]:
                grid[x][y] = 0
                coordinates.append((i, j))
                for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    check_neighbor(x + a, y + b, i + a, j + b, coordinates)
                return coordinates
            return False

        distinct = dict()
        for x in range(x_len):
            for y in range(y_len):
                island_shape = check_neighbor(x, y, 0, 0, [(0, 0)])
                if island_shape:
                    distinct[tuple(island_shape)] = 1

        return len(distinct)
