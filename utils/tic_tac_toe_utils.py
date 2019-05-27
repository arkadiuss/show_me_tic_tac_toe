def winning(board, move):
    return ((board[0][0] == move and board[0][1] == move and board[0][2] == move) or
            (board[1][0] == move and board[1][1] == move and board[1][2] == move) or
            (board[2][0] == move and board[2][1] == move and board[2][2] == move) or
            (board[0][0] == move and board[1][0] == move and board[2][0] == move) or
            (board[0][1] == move and board[1][1] == move and board[2][1] == move) or
            (board[0][2] == move and board[1][2] == move and board[2][2] == move) or
            (board[0][0] == move and board[1][1] == move and board[2][2] == move) or
            (board[2][0] == move and board[1][1] == move and board[0][2] == move))


def is_full(board):
    f = True
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                f = False
                break
    return f


def empty_fields(board):
    result = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                result.append([i, j])
    return result


# if wrong boards size  - -1
# the same - 0
# not the same - c (1<=c<=9) (number of diffs) and positions
def diff(board1, board2):
    if len(board1) != len(board2):
        return -1, []

    diffs = []
    for i in range(len(board1)):
        if len(board1[i]) != len(board2[i]):
            return -1, []
        for j in range(len(board1[i])):
            if board1[i][j] != board2[i][j]:
                diffs.append((i,j))

    return len(diffs), diffs

