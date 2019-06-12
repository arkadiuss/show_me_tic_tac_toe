

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

