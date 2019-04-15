from models.player import Player
from models.state import State


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def move(self, state: State):
        return input()
