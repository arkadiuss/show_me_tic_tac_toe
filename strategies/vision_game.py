from players.vision.human_player import HumanPlayer
from players.vision.computer_player import ComputerPlayer
from state.vision_state import VisionState
from strategies.game_strategy import GameStrategy


class VisionHumanPlayersGame(GameStrategy):

    def __init__(self):
        super().__init__(
            players=[HumanPlayer(name="Mikolaj", symbol='x'), ComputerPlayer(name="Arek", symbol='o')],
            state=VisionState(3, moves=['x', 'o']))

    def introduce(self):
        return "Vision game is a future. Now please show me the board."
