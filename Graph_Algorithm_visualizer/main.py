import networkx as nx
from shortest_path import Dijkstra
from Graph_visualizer import GraphVisualizer
from Minimum_Spanning_Tree import MSTAlgorithm
from DFS import DFSAlgorithm
from Custom import CustomAlgorithm
from BFS import BFSAlgorithm

print("May i Know which type of Graph you are trying to build? ")

print("Press 1 for undirected Graph || Press 2 for Directed Graph || Press 3 for MultiGraph(Undirected) || Press 4 for MultiGraph(Directed)")

Graph_type= int(input())

# Creating Graph
if Graph_type==1:
    graph = nx.Graph()
elif Graph_type==2:
    graph = nx.DiGraph()
elif Graph_type==3:
    graph = nx.MultiGraph()
else:
    graph=nx.MultiDiGraph()
    

n= int(input("No.of Nodes: "))
for i in range(0,n+1):
    graph.add_node(i)

m=int(input("No.of Edges: "))

weighted= int(input("Is is weighted Graph? Enter: 1 or 0 "))

print("Enter Edges: ")
for i in range(0,m):
    print("Enter Nodes: ")
    u=int(input("u = "))
    v=int(input("v = "))
    
    if weighted:
        w=int(input("Enter Weight: "))
    else:
        w=1    #Default
    graph.add_edge(u,v,weight=w)


print("Enter which Algorithm which u want to Visualize on your test Case?")
print("1 Shortest Path between Source and Destination(Dijkstra) || 2) Minimum Spanning Tree(Kruskal) || 3) Custom  ")
choice= int(input())

if choice == 1:    #Shortest Path
    # Choose the source and destination nodes
    source = int(input("Source: "))
    destination = int(input("Destination: "))
    

    algorithm= Dijkstra()    # for shortest path
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm, source, destination)

    
elif choice == 2: # Minimum Spanning Tree
    algorithm=MSTAlgorithm()
    visualizer = GraphVisualizer(graph)
    visualizer.visualize(algorithm)

elif choice == 3:
    algorithm= DFSAlgorithm()
    visualizer= GraphVisualizer(graph)
    visualizer.visualize(algorithm)

elif choice == 4:
    algorithm= BFSAlgorithm()
    visualizer= GraphVisualizer(graph)
    visualizer.visualize(algorithm)
    
else:
    extra= int(input("Are there any extra inputs? 1 or 0 "))
    algorithm = CustomAlgorithm(extra,n)
    visualizer= GraphVisualizer(graph)
    visualizer.visualize(algorithm)
    
    








