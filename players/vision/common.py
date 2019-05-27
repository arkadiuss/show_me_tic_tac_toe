from errors.move_error import MoveError
from state.state import State
from utils.tic_tac_toe_utils import diff


def wait_for_move(prevboard, state: State, expected_move):
    pboard = prevboard
    board = state.board()
    while True:
        d, diffs = diff(pboard, board)
        print(d, diffs, pboard, board)
        if d == 1:
            dr, dc = diffs[0]
            if pboard[dr][dc] != 0:
                raise MoveError
            if board[dr][dc] != expected_move:
                raise MoveError
            return dr, dc
        elif d > 1:
            raise MoveError
        pboard = board
        board = state.board()
