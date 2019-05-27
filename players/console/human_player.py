from players.player import Player
from state.state import State


class HumanPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)

    def move(self, state: State, opponent: Player):
        correct_input = False
        board = state.board()
        while not correct_input:
            movement = input()
            if len(movement) > 1:
                raise TypeError("Wrong input!\n")
            if ord(movement) < 48 or ord(movement) > 56:
                raise TypeError("Wrong input!\n")
            movement = int(movement, 10)
            if board[movement // len(board)][movement % len(board)] != 0:
                print("This field is busy!\nWrite correct number of field.\n")
                print(state)
            else:
                correct_input = True
        state.move(movement//len(board), movement % len(board), self.symbol)
