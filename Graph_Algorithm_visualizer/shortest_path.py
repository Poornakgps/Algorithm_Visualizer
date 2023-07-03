import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Dijkstra:
    def __init__(self):
        self.visited = set()
        self.distances = {}
        self.previous = {}
        self.shortest_path = []

    def execute(self, graph,pos,ax, source, destination):


        self._dijkstra(graph, source, destination,pos, ax)

        if destination not in self.distances:
            print(f"No path found from {source} to {destination}")
        else:
            self._build_shortest_path(source, destination)
            print(f"Shortest path from {source} to {destination}: {self.shortest_path}")


            node_colors = ['green' if n in self.shortest_path else 'white' for n in graph.nodes]
            nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
            nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
            self._draw_edges(graph, pos, ax)
            plt.title(f"Shortest Path: {self.shortest_path}")
            plt.draw()
            plt.pause(3)

    def _dijkstra(self, graph, source, destination, pos, ax):
        self.distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            dist, current_node = heapq.heappop(priority_queue)

            if current_node == destination:
                break

            if current_node not in self.visited:
                self.visited.add(current_node)

                for neighbor, weight_dict in graph[current_node].items():
                    weight = weight_dict['weight']
                    new_distance = self.distances[current_node] + weight

                    if neighbor not in self.distances or new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.previous[neighbor] = current_node
                        heapq.heappush(priority_queue, (new_distance, neighbor))
                        self._visualize(graph, pos, ax, neighbor)

    def _visualize(self,graph, pos, ax, neighbor):
        node_colors = ['green' if n == neighbor else 'lightblue' for n in graph.nodes]
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
        self._draw_edges(graph, pos, ax)
        plt.title(f"Current Node: {neighbor}")
        plt.draw()
        plt.pause(3)

    def _build_shortest_path(self, source, destination):
        current_node = destination
        self.shortest_path = [current_node]

        while current_node != source:
            current_node = self.previous[current_node]
            self.shortest_path.insert(0, current_node)

    def _draw_edges(self, graph, pos, ax):
        edge_colors = ['orange' if edge in self.shortest_path else 'blue' for edge in graph.edges()]
        nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5, edge_color=edge_colors)




    