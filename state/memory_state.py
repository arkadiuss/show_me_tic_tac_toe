from state.state import State
from utils.tic_tac_toe_utils import winning, is_full


class MemoryState(State):

    def __init__(self, board, moves):
        self._board = board
        self.moves = moves

    def __str__(self):
        result = ""
        for i in range(0, len(self._board)):
            for j in range(0, len(self._board)):
                result += str(self._board[i][j])
                if j < len(self._board)-1:
                    result += " "
            result += "\n"
        return result

    def board(self):
        return self._board

    def end(self):
        for m in self.moves:
            if self._winning(m):
                return True
        return self._is_full()

    def result(self):
        for m in self.moves:
            if self._winning(m):
                return "Player " + m + "is winning"
        return "Tie"

    def _is_full(self):
        return is_full(self._board)

    def _winning(self, move):
        return winning(self._board, move)

    def move(self, r, c, move):
        self._board[r][c] = move
