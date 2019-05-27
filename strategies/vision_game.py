from models.human_vision_player import HumanVisionPlayer
from state.vision_state import VisionState
from strategies.game_strategy import GameStrategy


class VisionHumanPlayersGame(GameStrategy):

    def __init__(self):
        super().__init__(
            players=[HumanVisionPlayer(name="Mikolaj", symbol='x'), HumanVisionPlayer(name="Arek", symbol='o')],
            state=VisionState(3, moves=['x', 'o']))
