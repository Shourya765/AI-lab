# Lab 02: DFS, BFS, Hill Climbing, and A* Search

## Aim
Implement and compare uninformed and heuristic search strategies on a state-space graph.

## Objectives
- Implement Depth First Search (DFS) using a stack.
- Implement Breadth First Search (BFS) using a queue.
- Implement hill climbing using a heuristic.
- Implement A* using path cost and heuristic cost.
- Observe that different strategies may return different paths.

## Algorithm / steps
1. Represent the state space as a graph with positive edge costs.
2. Run DFS and BFS from the start state, tracking visited nodes and parents.
3. Run hill climbing by choosing the neighboring state with the lowest heuristic value.
4. Run A* by expanding the state with the smallest `g(n) + h(n)` score.
5. Reconstruct and print each route. DFS, BFS, and hill climbing are not guaranteed to return a least-cost route.

## Source code
See [`main.py`](./main.py). The graph and heuristic are small examples for demonstrating the strategies.

## Run and output
Run `python main.py`. The program prints the route found by each strategy and its edge cost.

## Result and conclusion
DFS and BFS explore without using edge costs or a heuristic; BFS is shortest in number of edges for an unweighted graph. Hill climbing makes a locally greedy choice and can get stuck. A* combines accumulated path cost and heuristic guidance; with an admissible heuristic, it can find an optimal route.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
