class State:

    def __init__(self, board):
        self.board = board

    def __str__(self):
        result = ""
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                result += str(self.board[i][j])
                if j < len(self.board)-1:
                    result += " "
            result += "\n"
        return result

    def tie(self):
        is_full = True
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 0:
                    is_full = False
                    break
        return is_full

    def winning(self, player):
        if ((self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player) or
            (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player) or
            (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or
            (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player) or
            (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player) or
            (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player) or
            (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or
            (self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player)):
            return True
        else:
            return False
