"""Demonstrate DFS, BFS, hill climbing, and A* on a weighted graph."""

from collections import deque
from heapq import heappop, heappush


GRAPH = {
    "S": {"A": 1, "B": 4},
    "A": {"S": 1, "G": 10},
    "B": {"S": 4, "G": 2},
    "G": {"A": 10, "B": 2},
}
HEURISTIC = {"S": 3, "A": 1, "B": 2, "G": 0}


def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))


def path_cost(path):
    return sum(GRAPH[left][right] for left, right in zip(path, path[1:]))


def depth_first_search(start, goal):
    stack = [start]
    parent = {start: None}
    while stack:
        node = stack.pop()
        if node == goal:
            return reconstruct_path(parent, goal)
        for neighbor in reversed(list(GRAPH[node])):
            if neighbor not in parent:
                parent[neighbor] = node
                stack.append(neighbor)
    return None


def breadth_first_search(start, goal):
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            return reconstruct_path(parent, goal)
        for neighbor in GRAPH[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None


def hill_climbing(start, goal):
    path = [start]
    visited = {start}
    current = start
    while current != goal:
        candidates = [
            neighbor for neighbor in GRAPH[current]
            if neighbor not in visited
        ]
        if not candidates:
            return None
        next_node = min(candidates, key=lambda node: HEURISTIC[node])
        if HEURISTIC[next_node] >= HEURISTIC[current]:
            return None
        path.append(next_node)
        visited.add(next_node)
        current = next_node
    return path


def a_star_search(start, goal):
    frontier = [(HEURISTIC[start], 0, start)]
    parent = {start: None}
    best_cost = {start: 0}
    while frontier:
        _, cost, node = heappop(frontier)
        if cost != best_cost[node]:
            continue
        if node == goal:
            return reconstruct_path(parent, goal)
        for neighbor, edge_cost in GRAPH[node].items():
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                parent[neighbor] = node
                heappush(frontier, (new_cost + HEURISTIC[neighbor],
                                    new_cost, neighbor))
    return None


def main():
    searches = [
        ("DFS", depth_first_search),
        ("BFS", breadth_first_search),
        ("Hill climbing", hill_climbing),
        ("A*", a_star_search),
    ]
    for label, search in searches:
        route = search("S", "G")
        if route is None:
            print(f"{label}: no route found")
        else:
            print(f"{label}: {' -> '.join(route)} (cost {path_cost(route)})")


if __name__ == "__main__":
    main()
