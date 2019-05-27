from state.state import State


class MemoryState(State):

    def __init__(self, board, moves):
        super().__init__(moves)
        self._board = board

    def board(self):
        return self._board

    def move(self, r, c, move):
        self._board[r][c] = move
