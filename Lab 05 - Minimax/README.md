# Lab 05: Minimax Algorithm for Game Playing

## Aim
Implement the minimax algorithm to select moves in a two-player, zero-sum game.

## Objectives
- Represent a Tic-Tac-Toe board and enumerate legal moves.
- Evaluate terminal states for both players.
- Choose an optimal move assuming both players play optimally.
- Use alpha-beta pruning to avoid searching branches that cannot affect the result.

## Algorithm / steps
1. Check whether the board is a win, loss, or draw and return its score.
2. For each legal move, recursively evaluate the resulting board for the opponent.
3. The maximizing player chooses the highest score; the minimizing player chooses the lowest.
4. Update alpha and beta bounds and stop exploring a branch when `alpha >= beta`.
5. Print the best move and score for the sample position.

## Source code
See [`main.py`](./main.py). The board uses indices 0–8, read left to right and top to bottom.

## Run and output
Run `python main.py`. The program prints a best move for `X` and its minimax score.

## Result and conclusion
Minimax selects a move based on the assumption that the opponent responds optimally. Alpha-beta pruning preserves the selected result while reducing the number of game states evaluated.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
