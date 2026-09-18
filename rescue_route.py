from collections import deque
import heapq

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["H"],
    "F": ["I"],
    "G": ["J"],
    "H": ["K"],
    "I": ["K"],
    "J": ["K"],
    "K": ["L"],
    "L": []
}

cost = {
    "A": {"B": 2, "C": 5},
    "B": {"D": 4, "E": 2},
    "C": {"F": 1, "G": 3},
    "D": {"H": 3},
    "E": {"H": 1},
    "F": {"I": 5},
    "G": {"J": 2},
    "H": {"K": 1},
    "I": {"K": 1},
    "J": {"K": 1},
    "K": {"L": 2}
}


def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for next_node in graph[node]:
                queue.append(path + [next_node])

    return None


def ucs(start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        current_cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, current_cost

        if node in visited:
            continue

        visited.add(node)

        for next_node in graph[node]:
            new_cost = current_cost + cost[node][next_node]
            heapq.heappush(queue, (new_cost, path + [next_node]))

    return None, None


def dls(node, goal, depth, path):
    if node == goal:
        return path

    if depth == 0:
        return None

    for next_node in graph[node]:
        if next_node not in path:
            result = dls(
                next_node,
                goal,
                depth - 1,
                path + [next_node]
            )

            if result:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        result = dls(start, goal, depth, [start])

        if result:
            return result

        depth += 1


start = "A"
goal = "L"

bfs_path = bfs(start, goal)
ucs_path, minimum_cost = ucs(start, goal)
ids_path = ids(start, goal)

print("BFS Path:", bfs_path)
print("UCS Path:", ucs_path)
print("Minimum Cost:", minimum_cost)
print("IDS Path:", ids_path)

readme = '''# AI Practical Task – Emergency Rescue Route Planner

## Day-1

### Objective

#Develop a Python-based Emergency Rescue Route Planner where an emergency rescue robot acts as an intelligent agent.

#The robot starts from location **A (Entrance)** and must reach **L (Patient Location)** using different search algorithms.

## Environment

- A = Entrance
- B, C, D, E, F, G, H, I, J, K = Intermediate locations
- L = Patient location

## Graph

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["H"],
    "F": ["I"],
    "G": ["J"],
    "H": ["K"],
    "I": ["K"],
    "J": ["K"],
    "K": ["L"],
    "L": []
}
'''