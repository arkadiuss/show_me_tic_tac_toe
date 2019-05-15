from abc import ABC, abstractmethod

from state.state import State


class Player(ABC):

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    @abstractmethod
    def move(self, other, state: State):
        pass
