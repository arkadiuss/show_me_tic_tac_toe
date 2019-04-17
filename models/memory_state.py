from models.state import State


class MemoryState(State):

    def __init__(self, board, moves):
        self.board = board
        self.moves = moves

    def __str__(self):
        result = ""
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                result += str(self.board[i][j])
                if j < len(self.board)-1:
                    result += " "
            result += "\n"
        return result

    def board(self):
        return self.board

    def end(self):
        for m in self.moves:
            if self.winning(m):
                return True
        return self.tie()

    def result(self):
        for m in self.moves:
            if self.winning(m):
                return "Player " + m + "is winning"
        return "Tie"

    def tie(self):
        is_full = True
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 0:
                    is_full = False
                    break
        return is_full

    def winning(self, move):
        return ((self.board[0][0] == move and self.board[0][1] == move and self.board[0][2] == move) or
            (self.board[1][0] == move and self.board[1][1] == move and self.board[1][2] == move) or
            (self.board[2][0] == move and self.board[2][1] == move and self.board[2][2] == move) or
            (self.board[0][0] == move and self.board[1][0] == move and self.board[2][0] == move) or
            (self.board[0][1] == move and self.board[1][1] == move and self.board[2][1] == move) or
            (self.board[0][2] == move and self.board[1][2] == move and self.board[2][2] == move) or
            (self.board[0][0] == move and self.board[1][1] == move and self.board[2][2] == move) or
            (self.board[2][0] == move and self.board[1][1] == move and self.board[0][2] == move))
