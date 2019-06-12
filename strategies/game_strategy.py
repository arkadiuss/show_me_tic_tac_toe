from players.player import Player


class GameStrategy:

    def __init__(self, players, state):
        self.players = players
        self.state = state

    def introduce(self):
        return "Let's play"
