class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        import copy
        if K == 0:
            return 1
        move = {(2,1), (1,2), (-1,2), (-2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)}
        chess_next = [[1]*N for i in range(N)]
        for count in range(K):
            chessBoard = copy.deepcopy(chess_next)
            for i in range(N):
                for j in range(N):
                    chess_next[i][j] = 0
                    for step in move:
                        if 0<= i+step[0] < N and 0<= j+step[1] < N:
                            chess_next[i][j] += chessBoard[i+step[0]][j+step[1]]
        return chess_next[r][c]/8**K
