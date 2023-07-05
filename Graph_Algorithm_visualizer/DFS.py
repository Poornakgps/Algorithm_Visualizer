import matplotlib.pyplot as plt
import networkx as nx
from Graph_visualizer import GraphVisualizer

class DFSAlgorithm:
    def __init__(self):
        self.visited = set()
        self.steps = []
        self.edge_count = {}

    def execute(self, graph, pos, ax):
        for node in graph.nodes():
            if node not in self.visited:
                self._dfs(node, graph, pos, ax)

    def _dfs(self, node, graph, pos, ax):
        self.visited.add(node)  # visited
        self.steps.append(node) # Traversal

        node_colors = ['blue' if n == node else 'white' for n in graph.nodes]  # Assigning colors to current node and remaing

        ax.clear() # Clearing the current plot
        
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
        self._draw_edges(graph, pos, ax)
        plt.title(f"DFS: {self.steps}")
        plt.draw()
        plt.pause(5)

        for neighbor in graph.neighbors(node):
            if neighbor not in self.visited:
                self.edge_count[(node, neighbor)] = self.edge_count.get((node, neighbor), 0) + 1
                self._dfs(neighbor, graph, pos, ax)

        self.steps.pop()
        for neighbor in graph.neighbors(node):
            if self.edge_count.get((node, neighbor), 0) > 0:
                self.edge_count[(node, neighbor)] -= 1

        ax.clear()
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
        self._draw_edges(graph, pos, ax)
        plt.title(f"DFS: {self.steps}")
        plt.draw()
        plt.pause(5)

    def _draw_edges(self, graph, pos, ax):
        edge_colors = []
        for edge in graph.edges():
            count = self.edge_count.get(edge, 0)
            color = 'green' if count == 0 else 'orange' if count == 1 else 'red'
            edge_colors.append(color)
        nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5, edge_color=edge_colors)