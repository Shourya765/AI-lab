# Lab 04: Basic Search Strategies for AI Problems

## Aim
Apply search techniques to the 8-puzzle, 8-queens, and Tic-Tac-Toe problems.

## Objectives
- Search an 8-puzzle state space using A* and Manhattan distance.
- Solve the 8-queens constraint problem with backtracking.
- Search Tic-Tac-Toe game states to select a winning move.

## Algorithm / steps
1. **8-puzzle:** use A* with the number of moves so far plus Manhattan distance; skip already-seen states reached at equal or higher cost. Invalid boards are rejected, and unsolvable boards return no solution without exploring the state space.
2. **8-queens:** place one queen per row, checking columns and diagonals; backtrack when no safe square remains.
3. **Tic-Tac-Toe:** generate legal moves and recursively evaluate terminal game states using minimax; choose the best move for `X`.

## Source code
See [`main.py`](./main.py). Each problem has a small demonstration state.

## Run and output
Run `python main.py`. The program prints an 8-puzzle solution, one valid 8-queens arrangement, and the selected Tic-Tac-Toe move.

## Result and conclusion
Search is shaped by each problem's state representation and constraints. Heuristics guide A*, backtracking efficiently prunes invalid queen placements, and game-tree search evaluates competing moves.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
