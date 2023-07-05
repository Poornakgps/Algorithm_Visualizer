import networkx as nx
from shortest_path import Dijkstra
from Graph_visualizer import GraphVisualizer
from Minimum_Spanning_Tree import MSTAlgorithm
from DFS import DFSAlgorithm
from Custom import CustomAlgorithm
from BFS import BFSAlgorithm


print("Please select the type of graph:")
print("1. Undirected Graph")
print("2. Directed Graph")
graph_type = int(input("Enter your choice (1 or 2): "))

# Creating the graph
if graph_type == 1:
    graph = nx.Graph()
elif graph_type == 2:
    graph = nx.DiGraph()

# Enter the number of nodes and edges
n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))

# Check if the graph is weighted
weighted = int(input("Is it a weighted graph? Enter 1 for yes, 0 for no: "))


# Adding nodes to the graph by default from 1 to n
for i in range(1, n + 1):
    graph.add_node(i)


print("Enter the edges:")
for i in range(m):
    print("Edge", i + 1)
    u = int(input("Enter the source node: "))
    v = int(input("Enter the destination node: "))

    if weighted:
        w = int(input("Enter the weight: "))
    else:
        w = 1  # Default weight is 1 for unweighted graphs

    graph.add_edge(u, v, weight=w)

# select the algorithm to visualize on the graph
print("Enter the algorithm you want to visualize on your test case:")
print("1. DFS Traversal")
print("2. BFS Traversal")
print("3. Shortest Path between Source and Destination (Dijkstra's Algorithm)")
print("4. Minimum Spanning Tree (Kruskal's Algorithm)")
print("5. Custom Algorithm")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    # DFS Traversal
    algorithm = DFSAlgorithm()
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm)

elif choice == 2:
    # BFS Traversal
    algorithm = BFSAlgorithm()
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm)

elif choice == 3:
    # Shortest Path
    source = int(input("Enter the source node: "))
    destination = int(input("Enter the destination node: "))

    algorithm = Dijkstra()  # Dijkstra's Algorithm for finding shortest paths
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm, source, destination)

elif choice == 4:
    # Minimum Spanning Tree
    algorithm = MSTAlgorithm()
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm)

else:
    # Custom Algorithm
    extra = int(input("Are there any extra inputs? Enter 1 for yes, 0 for no: "))
    algorithm = CustomAlgorithm(extra, n)
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm)
    








