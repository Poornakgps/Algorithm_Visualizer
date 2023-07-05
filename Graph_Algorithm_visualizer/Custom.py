import matplotlib.pyplot as plt
import networkx as nx
from Graph_visualizer import GraphVisualizer
from collections import deque

class CustomAlgorithm:
    def __init__(self, extra,n):
        self.cnt=0
        self.visited = set()
        self.n = n
        self.extra = extra
        self.steps = []
        self.edge_count = {}

    def execute(self, graph, pos, ax):
        # Initialize the algorithm
        # start_node = list(graph.nodes())[0]  # Choose any starting node
        if self.extra:
            k=int(input("Enter k :"))
            c=int(input("Enter c : "))
        D=self._bfs(graph,0, pos, ax)
        d=max(D)
        x=D.index(d)
        D2=self._bfs(graph,x, pos, ax)
        d2=max(D2)
        y=D2.index(d2)
        D3=self._bfs(graph,y, pos, ax)
        print(max([k*max(D2[i],D3[i])-c*D[i] for i in range(self.n)]))
        print(self.cnt) # Time complexity
        
        
    def _bfs(self,G,s, pos, ax):
        # self._visualize_graph(G, pos, ax, "Custom Algorithm")
        inf=10**30
        D=[inf]*len(G)
        D[s]=0
        dq=deque()
        dq.append(s)
        while dq:
            self.cnt+=1
            curr=dq[-1]
            self._visualize(G, curr,dq, pos, ax, "Custom Algorithm")
            x=dq.popleft()
            for y in G.neighbors(x):
                if D[y]>D[x]+1:
                    D[y]=D[x]+1
                    dq.append(y)
        return D

    def _visualize(self, graph,x, dq, pos, ax ,title):
        ax.clear()
        ax.set_title(title)

        edge_colors = []
        for edge in graph.edges():
            count = self.edge_count.get(edge, 0)
            color = 'green' if count == 0 else 'orange' if count == 1 else 'red'
            edge_colors.append(color)

        node_colors = ['red' if n == x  else 'white' for n in graph.nodes]
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, alpha=0.7)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5, edge_color=edge_colors)

        plt.title(f"{dq}")
        plt.draw()
        plt.pause(4)
        
    # def _termination_condition(self):
    #     # Define the termination condition for the algorithm
    #     # Return True if the algorithm should terminate, False otherwise
    #     return False
    
    def _traverse(self, graph, current_node,pos, ax):
        # Perform custom algorithm logic here
        # Update visited nodes and perform any necessary operations

        # Visualize the current state
        self._visualize_graph(graph, pos, ax, "Custom Algorithm")

        # Update edge count for traversed edges
        for neighbor in graph[current_node]:
            edge = (current_node, neighbor)
            self.edge_count[edge] = self.edge_count.get(edge, 0) + 1

        # Check termination condition and return if satisfied
        if self._termination_condition():
            return

        # Recursively call the algorithm on unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self._traverse(graph, neighbor, ax)