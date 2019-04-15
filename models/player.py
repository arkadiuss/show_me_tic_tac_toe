from abc import ABC, abstractmethod

from models.state import State


class Player(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self, state: State):
        pass
