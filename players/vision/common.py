from errors.move_error import MoveError
from model import Board
from state.state import State


def wait_for_move(prevboard: Board, state: State, expected_move):
    pboard = prevboard
    board = state.board()
    while True:
        d, diffs = pboard.diff(board)
        if d == 1:
            dr, dc = diffs[0]
            if pboard(dr, dc) != 0:
                raise MoveError("You can\'t put sign on busy field")
            if board(dr, dc) != expected_move:
                raise MoveError("It's not your sign")
            return dr, dc
        elif d > 1:
            raise MoveError("You can do only one move")
        pboard = board
        board = state.board()
