from copy import deepcopy
from typing import List

tras_table = {}


def empty_squares(board: List[int]) -> int:
    """Returns the number of empty squares of the board
    Args:
        board (List[int]): List representing a board

    Returns:
        int: Number of empty squares
    """
    return board.count(0)


def won(board: List[int]) -> int:
    """Checks for a won game.

    Args:
        board (List[int]): The board

    Returns:
        int: 1 if maximizing player won, -1 if he lost or 0 if it is a draw
    """

    winning_cond = [
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},
        {0, 4, 8},
        {2, 4, 6}
    ]
    max_p_idxs = {i for i in range(9) if board[i] == 1}
    min_p_idxs = {i for i in range(9) if board[i] == 2}
    for cond in winning_cond:
        if cond.issubset(max_p_idxs):
            return 1
        if cond.issubset(min_p_idxs):
            return -1
    return 0


def evaluate(board: List[int]) -> int:
    """Evaluates the Tic Tac Toe board and gives it a positive number if it's winning(for the maximizing player),
    a negative number if it is losing, or 0 if it's even

    Args:
        board (List[int]): List representing the current state of the board
    Returns:
        int: Score given to the input board
    """
    return won(board) * (empty_squares(board) + 1)


def minimax(board, alpha=-10, beta=10, is_me=True):

    if tuple(board) in tras_table:
        return tras_table[tuple(board)]

    if won(board) != 0 or empty_squares(board) == 0:
        res = evaluate(board), None
        tras_table[tuple(board)] = res
        return res

    next_turn = not is_me
    move = None
    if is_me:
        value = -10
        for i in range(9):
            if board[i] == 0:
                board_tmp = deepcopy(board)
                board_tmp[i] = 1
                new_val, _ = minimax(board_tmp, alpha, beta, next_turn)
                if new_val > value:
                    value = new_val
                    move = i
                if value >= beta:
                    break
                alpha = max(alpha, value)
    else:
        value = 10
        for i in range(9):
            if board[i] == 0:
                board_tmp = deepcopy(board)
                board_tmp[i] = 2
                new_val, _ = minimax(board_tmp, alpha, beta, next_turn)
                if new_val < value:
                    value = new_val
                    move = i
                if value <= alpha:
                    break
                beta = min(beta, value)

    return value, move


def get_best_move(board: List[str], player: str) -> int:
    """"""
    player_map = {"x": 1, "o": 2,
                  "-": 0} if player == "x" else {"x": 2, "o": 1, "-": 0}
    translated_board = [player_map[i] for i in board]
    move = minimax(translated_board)
    return move


def main():
    """Main function"""
    player = input()
    print("Engine playing as " + player)
    while True:
        board_string = input()
        print(get_best_move(list(board_string), player))


if __name__ == "__main__":
    main()
