from collections import defaultdict
import math


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristics = {}

    def add_edge(self, start, to, cost):
        self.graph[start].append((to, cost))
        self.graph[to].append((start, cost))

    def set_heuristics(self, node, value):
        self.heuristics[node] = value

    def ida_start(self, start, goal):
        def dfs(node, g, threshold, path):
            f = g + self.heuristics[node]
            if f > threshold:
                return f, None
            if node == goal:
                return g, path

            min_threshold = math.inf
            for neighbor, cost in self.graph[node]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    temp_cost, result_path = dfs(
                        neighbor, g + cost, threshold, new_path
                    )
                    if result_path:
                        return temp_cost, result_path
                    min_threshold = min(min_threshold, temp_cost)
            return min_threshold, None

        threshold = self.heuristics[start]
        path = [start]

        while True:
            temp_cost, result_path = dfs(start, 0, threshold, path)
            if result_path:
                return result_path, temp_cost
            if temp_cost == math.inf:
                return None, math.inf  # artinya ini tidak ada solusi ya guys
            threshold = temp_cost


instance = Graph()

instance.add_edge("S", "A", 7)
instance.add_edge("S", "B", 2)
instance.add_edge("A", "B", 3)
instance.add_edge("A", "D", 4)
instance.add_edge("B", "D", 4)
instance.add_edge("B", "H", 1)
instance.add_edge("C", "L", 2)
instance.add_edge("H", "F", 3)
instance.add_edge("H", "G", 2)
instance.add_edge("L", "I", 4)
instance.add_edge("L", "J", 4)
instance.add_edge("I", "K", 4)
instance.add_edge("J", "K", 4)
instance.add_edge("K", "E", 5)
instance.add_edge("G", "E", 2)


instance.set_heuristics("S", 10)
instance.set_heuristics("A", 9)
instance.set_heuristics("B", 7)
instance.set_heuristics("C", 8)
instance.set_heuristics("D", 8)
instance.set_heuristics("E", 0)
instance.set_heuristics("F", 6)
instance.set_heuristics("G", 3)
instance.set_heuristics("H", 6)
instance.set_heuristics("I", 4)
instance.set_heuristics("J", 4)
instance.set_heuristics("K", 3)
instance.set_heuristics("L", 6)

path, cost = instance.ida_start("S", "E")
print("Path", " -> ".join(path) if path else "No path found")
