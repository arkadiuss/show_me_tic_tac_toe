from players.console.computer_player import ComputerPlayer
from players.console.human_player import HumanPlayer
from state.memory_state import MemoryState
from strategies.game_strategy import GameStrategy


class ConsoleGame(GameStrategy):

    def __init__(self):
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(
            players=[HumanPlayer(name="Humek", symbol='x'), ComputerPlayer(name="Comp", symbol='o')],
            state=MemoryState(board, moves=['x', 'o']))

    def introduce(self):
        return "Console game is also a good game. Let's play!"


