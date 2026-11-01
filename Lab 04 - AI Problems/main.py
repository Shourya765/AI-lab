"""Search demonstrations for 8-puzzle, 8-queens, and Tic-Tac-Toe."""

from heapq import heappop, heappush


GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan(state):
    distance = 0
    for index, tile in enumerate(state):
        if tile:
            goal_index = tile - 1
            distance += abs(index // 3 - goal_index // 3)
            distance += abs(index % 3 - goal_index % 3)
    return distance


def puzzle_neighbors(state):
    blank = state.index(0)
    row, column = divmod(blank, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = row + dr, column + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            other = nr * 3 + nc
            next_state = list(state)
            next_state[blank], next_state[other] = next_state[other], next_state[blank]
            yield tuple(next_state)


def solve_puzzle(start):
    start = tuple(start)
    if (len(start) != 9
            or any(type(tile) is not int for tile in start)
            or set(start) != set(GOAL)):
        raise ValueError("The puzzle must contain each integer from 0 to 8 once.")

    tiles = [tile for tile in start if tile]
    inversions = sum(
        tiles[i] > tiles[j]
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
    )
    if inversions % 2:
        return None

    frontier = [(manhattan(start), 0, start)]
    parents = {start: None}
    costs = {start: 0}
    while frontier:
        _, cost, state = heappop(frontier)
        if cost != costs[state]:
            continue
        if state == GOAL:
            route = []
            current = state
            while current is not None:
                route.append(current)
                current = parents[current]
            return list(reversed(route))
        for neighbor in puzzle_neighbors(state):
            new_cost = cost + 1
            if new_cost < costs.get(neighbor, float("inf")):
                costs[neighbor] = new_cost
                parents[neighbor] = state
                heappush(frontier, (new_cost + manhattan(neighbor),
                                    new_cost, neighbor))
    return None


def solve_queens(size=8):
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise ValueError("Board size must be a non-negative integer.")

    positions = []

    def place(row):
        if row == size:
            return True
        for column in range(size):
            if all(column != prior_column
                   and abs(column - prior_column) != row - prior_row
                   for prior_row, prior_column in enumerate(positions)):
                positions.append(column)
                if place(row + 1):
                    return True
                positions.pop()
        return False

    return positions.copy() if place(0) else None


def minimax(board, player):
    if len(board) != 9 or any(cell not in ("X", "O", " ") for cell in board):
        raise ValueError("The board must contain nine cells marked X, O, or space.")
    if player not in ("X", "O"):
        raise ValueError("Player must be 'X' or 'O'.")

    winner = get_winner(board)
    if winner == "X":
        return 1, None
    if winner == "O":
        return -1, None
    if " " not in board:
        return 0, None
    best_score = -2 if player == "X" else 2
    best_move = None
    next_player = "O" if player == "X" else "X"
    for index, cell in enumerate(board):
        if cell == " ":
            board[index] = player
            score, _ = minimax(board, next_player)
            board[index] = " "
            if (player == "X" and score > best_score) or (
                    player == "O" and score < best_score):
                best_score, best_move = score, index
    return best_score, best_move


def get_winner(board):
    lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def main():
    start = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    solution = solve_puzzle(start)
    if solution is None:
        print("8-puzzle has no solution.")
    else:
        print(f"8-puzzle solution length: {len(solution) - 1} moves")
        for state in solution:
            print(state[:3], state[3:6], state[6:])

    queens = solve_queens()
    print(f"8-queens solution (column per row, 0-based): {queens}")

    board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
    _, move = minimax(board, "X")
    print(f"Tic-Tac-Toe best move for X (0-based cell): {move}")


if __name__ == "__main__":
    main()
