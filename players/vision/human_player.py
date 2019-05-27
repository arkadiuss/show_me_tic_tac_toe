from players.player import Player
from state.state import State
from players.vision.common import wait_for_move


class HumanPlayer(Player):

    def move(self, state: State, opponent):
        print("Waiting for {0} move".format(self.name))
        wait_for_move(state, self.symbol)
        print("{0} has done a move".format(self.name))

