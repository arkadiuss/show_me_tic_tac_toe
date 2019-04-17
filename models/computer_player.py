from models.player import Player
from models.state import State


def empty_fields(state: State):
    result = []
    for i in range(0, len(state.board)):
        for j in range(0, len(state.board)):
            if state.board[i][j] == 0:
                result.append([i, j])
    return result


class Move:
    def __init__(self, index, score):
        self.index = index
        self.score = score


def optimum_move(computer, human, state: State, player):
    available_spots = empty_fields(state)
    if state.winning(player) and player != computer:
        return Move(None, -10)  # when computer loses -> move.score = -10
    elif state.winning(player):
        return Move(None, 10)   # when computer wins -> move.score = 10
    elif len(available_spots) == 0:
        return Move(None, 0)    # when there is no more fields -> tie

    moves = []

    for i in range(0, len(available_spots)):
        index = available_spots[i]
        state.board[available_spots[i][0]][available_spots[i][1]] = player  # simulation
        if player == computer:
            result = optimum_move(computer, human, state, human)
        else:
            result = optimum_move(computer, human, state, computer)
        state.board[available_spots[i][0]][available_spots[i][1]] = 0   # back to previous state
        moves.append(Move(index, result.score))     # creating a list of potential best moves

    # choosing best move for current player
    if player == computer:
        best_score = -10000
        for i in range(0, len(moves)):
            if moves[i].score > best_score:
                 best_score = moves[i].score
                 best_move = i
    else:
        best_score = 10000
        for i in range(0, len(moves)):
            if moves[i].score < best_score:
                 best_score = moves[i].score
                 best_move = i
                
    return moves[best_move]


class ComputerPlayer(Player):

    def __init__(self, symbol, name):
        super().__init__(symbol, name)

    def move(self, human, state: State):
        movement = optimum_move(self.symbol, human.symbol, state, self.symbol).index
        state.board[movement[0]][movement[1]] = self.symbol
