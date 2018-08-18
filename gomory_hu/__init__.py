# Gomory-Hu Tree Data Structure Implementation
# using Gusfield Algorithm
# Author: Marios Papachristou
# Date: August 2018

from collections import deque
from sys import maxsize as maxint

BLACK = 2
GRAY = 1
WHITE = 0


class GomoryHuTree:

    def __init__(self, graph):
        self.V = len(graph)
        self.capacity = {}
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = graph[i][j]
        self.color = {}
        self.pred = {}
        self.tree = {}
        self.flow = {}
        self.depth = {}

        self.build()
        self.prepare()

    def __repr__(self):
        return self.tree

    def __str__(self):
        return str(self.tree)

    def __getitem__(self, pos):
        i, j = pos
        return self.tree[i, j]

    def bfs(self, start, target):
        """Breadth-First Search between start and target"""
        
        for u in range(self.V):
            self.color[u] = WHITE
            self.depth[u] = -1

        q = deque()
        q.append(start)
        self.depth[start] = 0

        self.pred[start] = -1

        while q:
            u = q.popleft()
            self.color[u] = BLACK

            for v in range(self.V):
                if self.color[v] == WHITE and self.capacity[u,
                                                            v] - self.flow[u, v] > 0:
                    self.color[v] = GRAY
                    q.append(v)
                    self.pred[v] = u
                    self.depth[v] = self.depth[u] + 1

        return self.color[target] == BLACK

    def max_flow(self, source, sink):
        """Find maximum flow / minimum cut between source and sink with Ford Fulkerson"""

        max_flow = 0

        for i in range(self.V):
            for j in range(self.V):
                self.flow[i, j] = 0

        while self.bfs(source, sink):
            increment = maxint

            u = sink

            while self.pred[u] != -1:
                increment = min(
                    increment, self.capacity[self.pred[u], u] - self.flow[self.pred[u], u])
                u = self.pred[u]

            u = sink

            while self.pred[u] != -1:
                self.flow[self.pred[u], u] += increment
                self.flow[u, self.pred[u]] -= increment
                u = self.pred[u]

            max_flow += increment

        return max_flow

    def build(self):
        """Construct GomoryHuTree"""
        p = []
        f1 = []

        for i in range(self.V):
            p.append(0)
            f1.append(0)
            for j in range(self.V):
                self.tree[i, j] = 0

        for s in range(1, self.V):

            t = p[s]

            min_cut = self.max_flow(s, t)

            f1[s] = min_cut

            for i in range(self.V):
                if i != s and p[i] == t and self.color[i] == BLACK:
                    p[i] = s

            if self.color[p[t]] == BLACK:
                p[s] = p[t]
                p[t] = s
                f1[s] = f1[t]
                f1[t] = min_cut

            if s == self.V - 1:
                for i in range(1, s + 1):
                    self.tree[i, p[i]] = f1[i]

    def prepare(self):
        """Prepare for querying"""
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = self.tree[i, j]

    def query(self, u, v):
        """Query GomoryHuTree"""
        return max(self.max_flow(u, v), self.max_flow(v, u))
