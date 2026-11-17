from collections import deque

class PushRelabel:
    """Push-Relabel (Goldberg-Tarjan / Preflow-Push) Algorithm for Maximum Flow."""
    def __init__(self, num_nodes: int):
        self.n = num_nodes
        self.capacity = [[0] * num_nodes for _ in range(num_nodes)]
        self.flow = [[0] * num_nodes for _ in range(num_nodes)]
        self.excess = [0] * num_nodes
        self.height = [0] * num_nodes

    def add_edge(self, fr: int, to: int, cap: int):
        """Adds a directed edge from fr to to with capacity cap."""
        self.capacity[fr][to] += cap

    def _push(self, u: int, v: int):
        """Pushes excess flow from vertex u to vertex v."""
        send = min(self.excess[u], self.capacity[u][v] - self.flow[u][v])
        self.flow[u][v] += send
        self.flow[v][u] -= send
        self.excess[u] -= send
        self.excess[v] += send

    def _relabel(self, u: int):
        """Increases the height of vertex u so it can push flow to a neighbor."""
        min_h = float('inf')
        for v in range(self.n):
            if self.capacity[u][v] - self.flow[u][v] > 0:
                min_h = min(min_h, self.height[v])
        if min_h < float('inf'):
            self.height[u] = min_h + 1

    def _discharge(self, u: int, s: int, t: int, active_queue: deque, in_queue: list):
        """Discharges excess flow at vertex u using push and relabel operations."""
        while self.excess[u] > 0:
            pushed = False
            for v in range(self.n):
                if self.capacity[u][v] - self.flow[u][v] > 0 and self.height[u] == self.height[v] + 1:
                    self._push(u, v)
                    pushed = True
                    if v != s and v != t and not in_queue[v]:
                        active_queue.append(v)
                        in_queue[v] = True
                    if self.excess[u] == 0:
                        break
            if not pushed:
                self._relabel(u)

    def max_flow(self, s: int, t: int) -> int:
        """Computes the maximum flow from source s to sink t."""
        self.height = [0] * self.n
        self.excess = [0] * self.n
        self.flow = [[0] * self.n for _ in range(self.n)]

        self.height[s] = self.n
        self.excess[s] = float('inf')

        active_queue = deque()
        in_queue = [False] * self.n

        # Initial preflow: saturate all outgoing edges from source
        for v in range(self.n):
            if self.capacity[s][v] > 0:
                self._push(s, v)
                if v != s and v != t and not in_queue[v]:
                    active_queue.append(v)
                    in_queue[v] = True

        # Process active vertices until no excess remains
        while active_queue:
            u = active_queue.popleft()
            in_queue[u] = False
            self._discharge(u, s, t, active_queue, in_queue)

        return sum(self.flow[s])


if __name__ == "__main__":
    # Sample 1
    network = PushRelabel(4)
    network.add_edge(0, 1, 10)
    network.add_edge(0, 2, 5)
    network.add_edge(1, 2, 15)
    network.add_edge(1, 3, 10)
    network.add_edge(2, 3, 10)
    print(f"Maximum Flow (Case 1): {network.max_flow(0, 3)}")

    # Sample 2
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
