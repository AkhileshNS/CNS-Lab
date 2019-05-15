
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    def add(self, a, b, size):
        self.graph.append([a, b, size])

    def print(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V  # Initialize to infinite for all
        dist[src] = 0

        # dist: [0, inf, inf, inf, inf]

        for i in range(self.V - 1):
            for a, b, size in self.graph:
                if dist[a] != float("Inf") and dist[a] + size < dist[b]:
                    dist[b] = dist[a] + size

        for a, b, size in self.graph:
            if dist[a] != float("Inf") and dist[a] + size < dist[b]:
                print("Graph contains negative weight cycle")
                return

        self.print(dist)


g = Graph(5)
g.add(0, 1, -1)
g.add(0, 2, 4)
g.add(1, 2, 3)
g.add(1, 3, 2)
g.add(1, 4, 2)
g.add(3, 2, 5)
g.add(3, 1, 1)
g.add(4, 3, -3)

g.bellman_ford(0)
