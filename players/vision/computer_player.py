from errors.move_error import MoveError
from players.ai.square_board import optimum_move
from players.player import Player
from players.vision.common import wait_for_move
from state.state import State
import pyttsx3


def say(engine, text):
    engine.say(text)
    engine.runAndWait()


def _number_name(num):
    if num == 1:
        return 'first'
    elif num == 2:
        return 'second'
    elif num == 3:
        return 'third'
    return num


def _symbol_name(symbol):
    if symbol == 'x':
        return 'cross'
    elif symbol == 'o':
        return 'circle'
    return 'empty'


class ComputerPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.speech_engine = pyttsx3.init()

    def move(self, state: State, opponent):
        say(self.speech_engine, "Now it's my turn! You will lose!")
        movement = optimum_move(state.board(), opponent.symbol, self.symbol, self.symbol).index
        r, c = movement
        say(self.speech_engine, "Please put {0} in {1} row and {2} column".format(_symbol_name(self.symbol), _number_name(r+1), _number_name(c + 1)))
        try:
            dr, dc = wait_for_move(state, self.symbol)
            if dr != r or dc != c:
                raise MoveError
        except MoveError:
            say(self.speech_engine, "You tried to lie me. I won't play with you!")
            raise MoveError
        say(self.speech_engine, "Thank you")
