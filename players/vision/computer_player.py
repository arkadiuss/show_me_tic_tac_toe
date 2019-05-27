from errors.move_error import MoveError
from players.ai.square_board import optimum_move
from players.player import Player
from players.vision.common import wait_for_move
from state.state import State
from speech import Speech, symbol_name, number_name


class ComputerPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.voice = Speech()

    def say(self, text):
        self.voice.say(text)

    def move(self, state: State, opponent):
        board = state.board()
        self.say("Now it's my turn! You will lose!")
        movement = optimum_move(board, opponent.symbol, self.symbol, self.symbol).index
        r, c = movement
        self.say("Please put {0} in {1} row and {2} column".format(
            symbol_name(self.symbol), number_name(r+1), number_name(c + 1)))
        try:
            dr, dc = wait_for_move(board, state, self.symbol)
            if dr != r or dc != c:
                raise MoveError
        except MoveError:
            self.say("You tried to lie me. I won't play with you!")
            raise MoveError
        self.say("Thank you")
