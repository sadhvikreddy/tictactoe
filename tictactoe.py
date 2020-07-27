"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = 0
    none = 0
    for i in board:
        for j in i:
            if j is None:
                none = none + 1
            elif j == X:
                turn = turn + 1
            else:
                turn = turn - 1
    # print(turn)
    if none == 9:
        return X
    elif turn == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for indexi, i in enumerate(board):
        for indexj, j in enumerate(i):
            if j is None:
                # print((indexi, indexj))
                action.add((indexi, indexj))
            else:
                pass
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resBoard = copy.deepcopy(board)
    if action is not None:
        Row = action[0]
        Column = action[1]
        play = player(resBoard)
        if resBoard[Row][Column] is None:
            resBoard[Row][Column] = play
        return resBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] is not None:
        # print("We have a Winner!")
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] is not None:
        # print("We have a Winner!")
        return board[0][2]
    elif board[0][0] == board[0][1] == board[0][2] is not None:
        # print("We have a Winner!")
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] is not None:
        # print("We have a Winner!")
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] is not None:
        # print("We have a Winner!")
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] is not None:
        # print("We have a Winner!")
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] is not None:
        # print("We have a Winner!")
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] is not None:
        # print("We have a Winner!")
        return board[0][2]
    else:
        # print("Game has no Winner")
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = False
    if winner(board) is not None:
        # print("Win Confirmed. Terminating Game...")
        win = True
    else:
        for i in board:
            if None in i:
                # print("Game in Progress...")
                win = False
                break
            else:
                # print("Its a Tie!,Terminating Game...")
                win = True
    return win


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def invertPlayer(player):
    if player == X:
        return O
    else:
        return X


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (0,0)

    if terminal(board):
        return None

    ply = player(board)
    if ply == X:
        v = -999
        for action in actions(board):
            a = MinV(result(board,action))
            if a > v:
                v = a
                optimal = action
        return optimal
    if ply == O:
        v = 999
        for action in actions(board):
            b = MaxV(result(board,action))
            if b < v:
                v = b
                optimal = action
        return optimal


def MaxV(board):
    if terminal(board):
        return utility(board)
    v = -999
    for action in actions(board):
        v = max(v, MinV(result(board, action)))
    return v


def MinV(board):
    if terminal(board):
        return utility(board)
    v = 999
    for action in actions(board):
        v = min(v, MaxV(result(board, action)))
    return v
