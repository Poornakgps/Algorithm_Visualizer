import networkx as nx
import matplotlib.pyplot as plt


class MSTAlgorithm:
    def __init__(self):
        self.mst = nx.Graph()
        self.visited = set()
        self.edge_count = {}

    def execute(self, graph, pos, ax):
        # Initialize the algorithm
        start_node = list(graph.nodes())[0]  # Choose any starting node
        self.visited.add(start_node)

        self._dfs(graph, start_node, pos, ax)

    def _dfs(self, graph, current_node,pos, ax):
        for neighbor, data in graph[current_node].items():
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.mst.add_edge(current_node, neighbor, weight=data['weight'])

                # Update the edge count dictionary for visualization
                edge = tuple(sorted((current_node, neighbor)))
                self.edge_count[edge] = self.edge_count.get(edge, 0) + 1

                # Visualize the current MST
                self._visualize_graph(graph, pos, ax, "Minimum Spanning Tree")

                # Recursively call DFS on the unvisited neighbor
                self._dfs(graph, neighbor,pos, ax)

    def _visualize_graph(self, graph, pos, ax, title):
        ax.clear()
        ax.set_title(title)

        node_colors = ['red' if n in self.visited else 'white' for n in graph.nodes]
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')

        edge_colors = []
        for edge in graph.edges():
            count = self.edge_count.get(edge, 0)
            color = 'green' if count == 0 else 'orange' if count == 1 else 'red'
            edge_colors.append(color)
        nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5, edge_color=edge_colors)

        plt.draw()
        plt.pause(3)


