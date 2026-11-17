# Dinic's Algorithm

## Algorithm Explanation

The Ford-Fulkerson method finds augmenting paths one by one using DFS or BFS, which can lead to slow convergence in networks with high or floating-point capacities. Dinic's Algorithm drastically speeds up this process by finding multiple augmenting paths simultaneously in polynomial time $ (O(V^2 E) $.

**Key Concepts:**

1. Residual Graph: Tracks remaining capacities along forward and backward edges.
2. Level Graph (BFS): Constructs a layered network from the source $s$ to the sink $t$ by assigning "levels" (shortest distance in terms of edge count) to each node. Edges only move from level $L$ to level $L+1$.
3. Blocking Flow (DFS): Finds a maximal set of augmenting paths within the level graph in a single DFS pass until no more flow can be pushed through the current level graph.
4. Iteration: Repeat the BFS level graph construction and DFS blocking flow search until the sink becomes unreachable from the source.

**How it works:**

1. Building the Residual Network: For every directed edge in the graph, the algorithm sets up a forward and a backward capacity initialized to zero. This allows the algorithm to "push back" flow if a better routing choice is found later.
2. Phase 1: Constructing the Level Graph (Using BFS): The algorithm runs a Breadth-First Search (BFS) starting from the source node ($s$) to assign "levels" (shortest distance in terms of edge hops) to each reachable node. If the sink node ($t$) is never reached during this BFS, it means no more augmenting paths exist, and the algorithm terminates.
3. Phase 2: Finding a Blocking Flow (Using DFS): Once the level graph is built, the algorithm uses Depth-First Search (DFS) to push as much flow as possible from $s$ to $t$. DFS is strictly restricted to move forward only from level $L$ to level $L+1$. It stops exploring a path the moment an edge becomes fully saturated.
4. Iterating Until Completion: Steps 2 and 3 repeat in a loop, each loop strictly increases the shortest distance from the source to the sink, ensuring the algorithm converges very quickly in polynomial time.

---

## Prerequisites

- **Python**: Python 3.8+ (tested on Python 3.12).
- **Dependencies**: **None** (Pure Python standard library modules are enough)

---

## Sample Input Output

_Used with algorithm implementation at `implementation.py`_

### Sample 1

```py
network = Dinic(4)
network.add_edge(0, 1, 10)
network.add_edge(0, 2, 5)
network.add_edge(1, 2, 15)
network.add_edge(1, 3, 10)
network.add_edge(2, 3, 10)

print(f"Maximum Flow (Case 1): {network.max_flow(0, 3)}")
# Output: Maximum Flow (Case 1): 15
```

### Sample 2

```py
network2 = Dinic(6)
network2.add_edge(0, 1, 16)
network2.add_edge(0, 2, 13)
network2.add_edge(1, 2, 10)
network2.add_edge(1, 3, 12)
network2.add_edge(2, 1, 4)
network2.add_edge(2, 4, 14)
network2.add_edge(3, 2, 9)
network2.add_edge(3, 5, 20)
network2.add_edge(4, 3, 7)
network2.add_edge(4, 5, 4)

print(f"Maximum Flow (Case 2): {network2.max_flow(0, 5)}")
# Output: Maximum Flow (Case 2): 23
```

## AI Disclosure

- AI Model used: Gemini
- Scope of assistance: Assisted in writing code implementation and sample cases
