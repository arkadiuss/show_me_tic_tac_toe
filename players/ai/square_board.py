from math import inf

from model import Board


class Move:
    def __init__(self, index, score):
        self.index = index
        self.score = score


def optimum_move(board: Board, opponent_move, player_move, cur_move):
    available_spots = board.empty_fields()
    if board.winning(opponent_move):
        return Move(None, -10)  # when computer loses -> move.score = -10
    elif board.winning(player_move):
        return Move(None, 10)  # when computer wins -> move.score = 10
    elif len(available_spots) == 0:
        return Move(None, 0)  # when there is no more fields -> tie

    moves = []

    for i in range(0, len(available_spots)):
        index = available_spots[i]
        board = board.put(available_spots[i][0],available_spots[i][1], cur_move)  # simulation
        if cur_move == player_move:
            result = optimum_move(board, opponent_move, player_move, opponent_move)
        else:
            result = optimum_move(board, opponent_move, player_move, player_move)
        board = board.put(available_spots[i][0], available_spots[i][1], 0)  # back to previous state
        moves.append(Move(index, result.score))  # creating a list of potential best moves

    # choosing best move for current player
    if cur_move == player_move:
        best_score = -inf
        for i in range(0, len(moves)):
            if moves[i].score > best_score:
                best_score = moves[i].score
                best_move = i
    else:
        best_score = inf
        for i in range(0, len(moves)):
            if moves[i].score < best_score:
                best_score = moves[i].score
                best_move = i

    return moves[best_move]
