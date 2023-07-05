import matplotlib.pyplot as plt
import networkx as nx
from Graph_visualizer import GraphVisualizer
from collections import deque

class BFSAlgorithm:
    def __init__(self):
        self.visited = set()
        self.steps = []
        self.edge_count = {}

    def execute(self, graph, pos, ax):
        for node in graph.nodes():
            if node not in self.visited:
                self._bfs(node, graph, pos, ax)

    def _bfs(self, start, graph, pos, ax):
        queue = deque([(start, None)])
        while queue:
            node, parent = queue.popleft()
            self.visited.add(node)
            self.steps.append(node)

            node_colors = ['lightblue' if n == node else 'white' for n in graph.nodes]

            ax.clear()
            nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
            nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
            self._draw_edges(graph, pos, ax)
            plt.title(f"BFS: {self.steps}")
            plt.draw()
            plt.pause(1)

            if parent is not None:
                self.edge_count[(parent, node)] = self.edge_count.get((parent, node), 0) + 1

            for neighbor in graph.neighbors(node):
                if neighbor not in self.visited:
                    queue.append((neighbor, node))

            ax.clear()
            nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
            nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
            self._draw_edges(graph, pos, ax)
            plt.title(f"BFS: {self.steps}")
            plt.draw()
            plt.pause(1)
            
    def _draw_edges(self, graph, pos, ax):
        edge_colors = []
        for edge in graph.edges():
            count = self.edge_count.get(edge, 0)
            color = 'green' if count == 0 else 'orange' if count == 1 else 'red'
            edge_colors.append(color)
        nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5, edge_color=edge_colors)