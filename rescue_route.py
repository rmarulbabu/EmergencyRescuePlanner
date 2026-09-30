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


# Breadth First Search
def bfs(start, goal):
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbour in graph[current]:
            queue.append(path + [neighbour])

    return None


# Uniform Cost Search
def ucs(start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        total_cost, path = heapq.heappop(queue)
        current = path[-1]

        if current == goal:
            return path, total_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbour in graph[current]:
            new_cost = total_cost + cost[current][neighbour]
            heapq.heappush(queue, (new_cost, path + [neighbour]))

    return None, None


# Depth Limited Search
def dls(current, goal, depth, path):
    if current == goal:
        return path

    if depth == 0:
        return None

    for neighbour in graph[current]:
        if neighbour not in path:
            result = dls(
                neighbour,
                goal,
                depth - 1,
                path + [neighbour]
            )

            if result:
                return result

    return None


# Iterative Deepening Search
def ids(start, goal):
    depth = 0

    while True:
        result = dls(start, goal, depth, [start])

        if result:
            return result

        depth += 1


start = "A"
goal = "L"

bfs_result = bfs(start, goal)
ucs_result, ucs_cost = ucs(start, goal)
ids_result = ids(start, goal)

print("BFS Path:", bfs_result)
print("UCS Path:", ucs_result)
print("Minimum Cost:", ucs_cost)
print("IDS Path:", ids_result)