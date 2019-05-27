from errors.move_error import MoveError
from players.ai.square_board import optimum_move
from players.player import Player
from players.vision.common import wait_for_move
from state.state import State


def _symbol_name(symbol):
    if symbol == 'x':
        return 'cross'
    elif symbol == 'o':
        return 'circle'
    return 'empty'


class ComputerPlayer(Player):

    def move(self, state: State, opponent):
        print("{0}: Now it's my turn! You will lose!".format(self.name))
        movement = optimum_move(state.board(), opponent.symbol, self.symbol, self.symbol).index
        r, c = movement
        print("Please put {0} on {1},{2}".format(_symbol_name(self.symbol), r, c))
        try:
            dr, dc = wait_for_move(state, self.symbol)
            if dr != r or dc != c:
                raise MoveError
        except MoveError:
            print("You tried to lie me. I won't play with you!")
            raise MoveError
        print("{0}: Thank you".format(self.name))
