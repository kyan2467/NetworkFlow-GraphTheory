# Push-Relabel Algorithm

## Algorithm Explanation

Unlike the Ford-Fulkerson method and Dinic's Algorithm which repeatedly search for complete augmenting paths from source to sink across the entire network, the **Push-Relabel Algorithm** (Goldberg-Tarjan) takes a fundamentally different, localized approach. It relaxes the flow conservation condition during execution by allowing vertices to hold an temporary "excess" of flow (called a **preflow**), and works strictly on local vertex neighborhoods.

**Key Concepts:**

1. **Preflow and Excess:** Vertices can temporarily have more incoming flow than outgoing flow. The difference is the vertex's *excess* $e(u)$. An intermediate node with $e(u) > 0$ is called *active*.
2. **Height Function (Distance Labels):** Each node $u$ is assigned an integer height $h(u)$. Flow is only permitted to move "downhill" across edges where $h(u) = h(v) + 1$. The source is initialized at height $h(s) = |V|$ and sink at $h(t) = 0$.
3. **Push Operation:** If a vertex $u$ is active and has a residual neighbor $v$ strictly below it ($h(u) = h(v) + 1$), it pushes $\min(e(u), c(u, v) - f(u, v))$ flow to $v$.
4. **Relabel Operation:** If an active vertex cannot push flow to any neighbor because its height is less than or equal to all residual neighbors, its height is increased ("relabeled") to $1 + \min \{h(v) \mid (u, v) \in E_f\}$ so that it can push flow in subsequent steps.
5. **Discharge (FIFO Queue):** Active vertices are processed from a FIFO queue, repeatedly pushing or relabeling until their excess reaches zero or they are placed back in the queue.

**How it works:**

1. **Initialization:** Set the height of the source to $h(s) = |V|$ and all other nodes to 0. Saturate all outgoing edges from the source $s$ with maximum capacity. The neighbors of $s$ receive positive excess and become active.
2. **Pushing Downhill:** Select an active node $u$ from the queue. Look for residual edges $(u, v)$ where $h(u) = h(v) + 1$. If found, push flow to $v$. If $v$ was not active and is not the sink/source, add $v$ to the active queue.
3. **Relabeling When Blocked:** If node $u$ still has excess but no neighbor is downhill, raise $h(u)$ to one above its lowest available residual neighbor.
4. **Termination:** Continue discharging active vertices until no active vertex remains. Any flow that cannot reach the sink eventually flows backwards uphill into the source $s$. The resulting preflow satisfies flow conservation and represents the maximum flow in $\mathcal{O}(V^3)$ time (using FIFO selection).

---

## Prerequisites

- **Python**: Python 3.8+ (tested on Python 3.12 / 3.14).
- **Dependencies**: **None** (Pure Python standard library modules are enough)

---

## Sample Input Output

_Used with algorithm implementation at `implementation.py`_

### Sample 1

```py
network = PushRelabel(4)
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
network2 = PushRelabel(6)
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

### Sample 3 (ITS Lecture Slide Network - Slide 4 & 10)

```py
# S=0, A=1, B=2, C=3, D=4, T=5
network3 = PushRelabel(6)
network3.add_edge(0, 1, 5)  # S -> A
network3.add_edge(0, 2, 2)  # S -> B
network3.add_edge(1, 3, 2)  # A -> C
network3.add_edge(1, 2, 2)  # A -> B
network3.add_edge(2, 4, 4)  # B -> D
network3.add_edge(4, 3, 1)  # D -> C
network3.add_edge(3, 5, 3)  # C -> T
network3.add_edge(4, 5, 5)  # D -> T

print(f"Maximum Flow (Case 3): {network3.max_flow(0, 5)}")
# Output: Maximum Flow (Case 3): 6
```

---

## AI Disclosure

- AI Model used: Gemini
- Scope of assistance: Assisted in writing code implementation, height function logic, and sample cases
