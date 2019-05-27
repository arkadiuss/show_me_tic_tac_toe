from models.player import Player
from state.state import State
from utils.tic_tac_toe_utils import diff


class HumanVisionPlayer(Player):

    def move(self, state: State, opponent):
        pboard = state.board()
        print("Waiting for {0} move".format(self.name))
        board = state.board()
        while True:
            d, diffs = diff(pboard, board)
            print(d)
            if d == 1:
                print("{0} has done a move".format(self.name))
                break
            elif d > 1:
                raise TypeError
            pboard = board
            board = state.board()
