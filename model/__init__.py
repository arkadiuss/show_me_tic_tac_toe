from copy import deepcopy

from utils.tic_tac_toe_utils import diff


class Board:

    def __init__(self, board):
        if any([len(b) != len(board) for b in board]):
            raise TypeError
        self._board = board

    def __call__(self, r, c):
        return self._board[r][c]

    def __len__(self):
        return len(self._board)

    def as_array(self):
        return self._board

    def winning(self, move):
        return ((self._board[0][0] == move and self._board[0][1] == move and self._board[0][2] == move) or
                (self._board[1][0] == move and self._board[1][1] == move and self._board[1][2] == move) or
                (self._board[2][0] == move and self._board[2][1] == move and self._board[2][2] == move) or
                (self._board[0][0] == move and self._board[1][0] == move and self._board[2][0] == move) or
                (self._board[0][1] == move and self._board[1][1] == move and self._board[2][1] == move) or
                (self._board[0][2] == move and self._board[1][2] == move and self._board[2][2] == move) or
                (self._board[0][0] == move and self._board[1][1] == move and self._board[2][2] == move) or
                (self._board[2][0] == move and self._board[1][1] == move and self._board[0][2] == move))

    def is_full(self):
        f = True
        for i in range(0, len(self)):
            for j in range(0, len(self)):
                if self._board[i][j] == 0:
                    f = False
                    break
        return f

    def empty_fields(self):
        result = []
        for i in range(0, len(self)):
            for j in range(0, len(self)):
                if self._board[i][j] == 0:
                    result.append([i, j])
        return result

    # if wrong boards size  - -1
    # the same - 0
    # not the same - c (1<=c<=9) (number of diffs) and positions
    def diff(self, board2):
        return diff(self._board, board2._board)

    def put(self, r, c, move):
        newboard = deepcopy(self._board)
        newboard[r][c] = move
        return Board(newboard)


