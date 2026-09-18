# Emergency Rescue Route Planner

An AI practical project that models an emergency rescue robot traveling from an entrance to a patient's location through a directed graph.

## Objective

Find a route from location `A` (entrance) to location `L` (patient) using three search strategies:

- **Breadth-First Search (BFS):** finds a path with the fewest edges.
- **Uniform-Cost Search (UCS):** finds the least-cost path using the defined travel costs.
- **Iterative Deepening Search (IDS):** repeatedly performs depth-limited search until it finds the goal.

## Environment

| Location | Meaning |
| --- | --- |
| `A` | Entrance |
| `B` through `K` | Intermediate locations |
| `L` | Patient location |

The directed graph is:

```text
A -> B, C
B -> D, E
C -> F, G
D -> H
E -> H
F -> I
G -> J
H -> K
I -> K
J -> K
K -> L
```

Travel costs are defined in `planner.py` and are used by UCS.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run

From the project directory, run:

```bash
python planner.py
```

The search implementation is executable directly from `planner.py`, so running the command prints the BFS path, UCS path, minimum cost, and IDS path.

## Project Files

- `planner.py` - stores the route-planning implementation and project notes.
- `README.md` - project documentation.

## Expected Search Results

For the configured graph, the search implementation returns:

```text
BFS Path: ['A', 'B', 'D', 'H', 'K', 'L']
UCS Path: ['A', 'B', 'E', 'H', 'K', 'L']
Minimum Cost: 8
IDS Path: ['A', 'B', 'D', 'H', 'K', 'L']
```
