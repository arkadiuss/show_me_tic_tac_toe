from players.player import Player
from state.state import State
from players.ai.square_board import optimum_move


class ComputerPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)

    def move(self, state: State, opponent: Player):
        movement = optimum_move(state.board(), opponent.symbol, self.symbol, self.symbol).index
        r, c = movement
        state.move(r, c, self.symbol)
