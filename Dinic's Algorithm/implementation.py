from collections import deque

class Edge:
    """Represents a directed edge in the residual network."""
    def __init__(self, to: int, cap: int, rev: int):
        self.to = to
        self.cap = cap
        self.rev = rev
        self.flow = 0

class Dinic:
    """Dinic's Algorithm implementation for Maximum Flow."""
    def __init__(self, num_nodes: int):
        self.n = num_nodes
        self.graph = [[] for _ in range(num_nodes)]
        self.level = []
        self.ptr = []

    def add_edge(self, fr: int, to: int, cap: int):
        """Adds a directed edge with capacity `cap` and its residual reverse edge."""
        forward = Edge(to, cap, len(self.graph[to]))
        backward = Edge(fr, 0, len(self.graph[fr]))
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def _bfs(self, s: int, t: int) -> bool:
        """Constructs the level graph using BFS."""
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = deque([s])
        
        while queue:
            v = queue.popleft()
            for edge in self.graph[v]:
                if edge.cap - edge.flow > 0 and self.level[edge.to] < 0:
                    self.level[edge.to] = self.level[v] + 1
                    queue.append(edge.to)
                    
        return self.level[t] >= 0

    def _dfs(self, v: int, t: int, pushed: int) -> int:
        """Finds a blocking flow in the level graph using DFS."""
        if pushed == 0:
            return 0
        if v == t:
            return pushed
            
        for cid in range(self.ptr[v], len(self.graph[v])):
            self.ptr[v] = cid
            edge = self.graph[v][cid]
            tr = edge.to
            
            if self.level[v] + 1 != self.level[tr] or edge.cap - edge.flow == 0:
                continue
                
            tr_pushed = self._dfs(tr, t, min(pushed, edge.cap - edge.flow))
            if tr_pushed == 0:
                continue
                
            edge.flow += tr_pushed
            self.graph[tr][edge.rev].flow -= tr_pushed
            return tr_pushed
            
        return 0

    def max_flow(self, s: int, t: int) -> int:
        """Computes the maximum flow from source s to sink t."""
        flow = 0
        while self._bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self._dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed
        return flow
