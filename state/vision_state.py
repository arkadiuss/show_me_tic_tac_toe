from model import Board
from state.state import State
import vision.state_reader as sr
from utils.tic_tac_toe_utils import diff


def _is_valid(board, board_size):
    if len(board) != board_size:
        return False
    for row in board:
        if len(row) != board_size:
            return False
    return True


class VisionState(State):

    def __init__(self, board_size, moves):
        super().__init__(moves)
        self.board_size = board_size
        sr.init()

    def board(self):
        threshold = 30
        board = sr.get_state()
        r = 0  # repeat - how many times was this state
        while not _is_valid(board, self.board_size) or r < threshold:
            pboard = board
            board = sr.get_state()
            if diff(pboard, board)[0] == 0:
                r += 1
            else:
                r = 0
        return Board(board)

    def move(self, r, c, move):
        pass

    def __del__(self):
        sr.destroy()
