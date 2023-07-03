import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.pos = None

    def visualize(self, algorithm, source=None, Destination=None):
        '''
        pos = nx.spring_layout(self.graph) is used to calculate the positions of the nodes in the graph layout. 
        spring_layout is a layout algorithm provided by the NetworkX library. It uses the Fruchterman-Reingold 
        force-directed algorithm to determine the positions of the nodes based on their connections.
        '''
        self.pos = nx.spring_layout(self.graph)
        '''
        fig, ax = plt.subplots(figsize=(8, 6)) is used to create a new figure and axes object for the plot. 
        It creates a new figure window with a specified size of 8 inches by 6 inches and returns the figure object fig 
        and the axes object ax. The fig object represents the entire figure window, and the ax object represents the axes 
        or plot area within the figure where the graph will be plotted.
        '''
        fig, ax = plt.subplots(figsize=(8, 6))
        
        plt.axis('off')

        nx.draw_networkx_nodes(self.graph, self.pos, node_color='blue', node_size=500, alpha=0.7)
        nx.draw_networkx_labels(self.graph, self.pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(self.graph, self.pos, width=1, alpha=0.5)

        plt.title("Initial Graph")
        plt.draw()
        plt.pause(1)
        
        # Executing algorithm
        if source==None:
            algorithm.execute(self.graph, self.pos, ax)  
        else:
            algorithm.execute(self.graph, self.pos, ax, source, Destination)

        plt.title("Final Graph")
        plt.pause(1)
        plt.show()