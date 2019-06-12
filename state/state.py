from abc import abstractmethod, ABC

from model import Board


class State(ABC):

    def __init__(self, moves):
        self.moves = moves

    def __str__(self):
        result = ""
        board = self.board()
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                result += str(board(i,j))
                if j < len(board) - 1:
                    result += " "
            result += "\n"
        return result

    @abstractmethod
    def board(self) -> Board:
        pass

    def end(self):
        for m in self.moves:
            if self._winning(m):
                return True
        return self._is_full()

    def result(self):
        for m in self.moves:
            if self._winning(m):
                return m
        return 0

    def _is_full(self):
        return self.board().is_full()

    def _winning(self, move):
        return self.board().winning(move)

    @abstractmethod
    def move(self, r, c, move):
        pass

