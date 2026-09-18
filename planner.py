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
    "H": {"K": 2},
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
                new_path = path + [next_node]
                queue.append(new_path)

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
            new_path = path + [next_node]
            heapq.heappush(queue, (new_cost, new_path))

    return None, None


def depth_limited_search(node, goal, depth, path):
    if node == goal:
        return path

    if depth == 0:
        return None

    for next_node in graph[node]:
        if next_node not in path:
            result = depth_limited_search(
                next_node,
                goal,
                depth - 1,
                path + [next_node]
            )

            if result is not None:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        result = depth_limited_search(
            start,
            goal,
            depth,
            [start]
        )

        if result is not None:
            return result

        depth += 1


start = "A"
goal = "L"

print("EMERGENCY RESCUE ROUTE PLANNER")
print("--------------------------------")

print("\nBFS:")
bfs_path = bfs(start, goal)
print("Path:", " -> ".join(bfs_path))

print("\nUCS:")
ucs_path, ucs_cost = ucs(start, goal)
print("Path:", " -> ".join(ucs_path))
print("Total Cost:", ucs_cost)

print("\nIDS:")
ids_path = ids(start, goal)
print("Path:", " -> ".join(ids_path))