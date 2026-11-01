"""Tic-Tac-Toe minimax with alpha-beta pruning."""


WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def minimax(board, player, alpha=-2, beta=2):
    result = winner(board)
    if result == "X":
        return 1, None
    if result == "O":
        return -1, None
    if " " not in board:
        return 0, None

    maximizing = player == "X"
    best_score = -2 if maximizing else 2
    best_move = None
    next_player = "O" if maximizing else "X"

    for move, cell in enumerate(board):
        if cell != " ":
            continue
        board[move] = player
        score, _ = minimax(board, next_player, alpha, beta)
        board[move] = " "

        if (maximizing and score > best_score) or (
                not maximizing and score < best_score):
            best_score, best_move = score, move

        if maximizing:
            alpha = max(alpha, best_score)
        else:
            beta = min(beta, best_score)
        if alpha >= beta:
            break
    return best_score, best_move


def print_board(board):
    for row in range(3):
        print(" | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("--+---+--")


def main():
    board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
    print("Current board:")
    print_board(board)
    score, move = minimax(board, "X")
    print(f"Best move for X: cell {move} (0-based index)")
    print(f"Minimax score: {score} (1 = X win, 0 = draw, -1 = O win)")
    board[move] = "X"
    print("Board after X's move:")
    print_board(board)


if __name__ == "__main__":
    main()
