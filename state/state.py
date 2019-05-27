from abc import abstractmethod, ABC


class State(ABC):
    @abstractmethod
    def board(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def move(self, r, c, move):
        pass

