from players.player import Player


class GameStrategy:

    def __init__(self, players, state):
        # TODO: add validation
        self.players = players
        self.state = state
