from models.player import Player
from state.state import State


class HumanPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)

    def move(self, computer, state: State):
        correct_input = False
        while not correct_input:
            movement = input()
            if len(movement) > 1:
                raise TypeError("Wrong input!\n")
            if ord(movement) < 48 or ord(movement) > 56:
                raise TypeError("Wrong input!\n")
            movement = int(movement, 10)
            if state.board[movement // len(state.board)][movement % len(state.board)] != 0:
                print("This field is busy!\nWrite correct number of field.\n")
                print(state)
            else:
                correct_input = True
        state.board[movement//len(state.board)][movement % len(state.board)] = self.symbol
