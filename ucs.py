from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, directed=True):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, start, to, sum_cost):
        if self.directed:
            self.graph[start].append((sum_cost, to))
        else:
            self.graph[to].append((sum_cost, start))

    def ucs(self, start_node, goal_node):
        close = set()
        queue = PriorityQueue()
        queue.put((0, start_node, [start_node]))

        while not queue.empty():
            current_cost, current_node, path = queue.get()

            if current_cost in close:
                continue

            close.add(current_node)

            if current_node == goal_node:
                print(" -> ".join(path))
                print(f"Total cost: {current_cost}")
                return

            for sum_cost, neighbour in self.graph[current_node]:
                if neighbour not in close:
                    queue.put((current_cost + sum_cost, neighbour, path + [neighbour]))


g = Graph(directed=True)

g.add_edge("S", "A", 3)
g.add_edge("S", "C", 2)
g.add_edge("A", "B", 1)
g.add_edge("A", "D", 3)
g.add_edge("C", "B", 5)
g.add_edge("C", "D", 6)
g.add_edge("B", "G", 7)
g.add_edge("D", "G", 1)

print(g.graph)
print(g.ucs("S", "G"))
