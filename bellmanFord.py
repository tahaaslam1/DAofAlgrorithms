from queue import PriorityQueue
from os import read
import networkx as nx
import matplotlib.pyplot as plt

class Bellman:
    def __init__(self, file):
        self.f = open(file)

    def show(self):
        firstline = self.f.readline()

        g = Graph(int(firstline))
        G = nx.Graph()
        P = nx.Graph()

        for i in range(0, int(firstline)):
            y = self.f.readline()
            y = y.split()
            node = [float(i) for i in y]
            vertice = node[0]
            x_cord = node[1]
            y_cord = node[2]
            print(vertice, x_cord, y_cord)
            G.add_node(vertice, pos = (x_cord, y_cord))
            P.add_node(vertice, pos = (x_cord, y_cord))

        for i in range (0, int(firstline)):
            y = self.f.readline()
            y = y.split()
            edge = [float(i) for i in y]
            for j in range(1,len(edge),4):
                print(edge[0], edge[j], edge[j+2])
                
                if edge[0] != edge[j]:
                    G.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)
                    g.addedge(int(edge[0]), int(edge[j]), float(edge[j+2]/10000000))


        pos = nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.figure(1)
        nx.draw(G, pos, with_labels = True)
        print(G)

        pos = nx.get_node_attributes(P,'pos')
        labels = nx.get_edge_attributes(P,'weight')
        print(labels)
        nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
        plt.figure(2)
        nx.draw(P, pos, with_labels = True)

        g.bellman_ford(4, P)

        plt.show()


class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def addedge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, src, dist, P):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
            P.add_edge(src, i, weight = dist[i])

        pos = nx.get_node_attributes(P,'pos')
        labels = nx.get_edge_attributes(P,'weight')
        print(labels)
        nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
        plt.figure(2)
        nx.draw(P, pos, with_labels = True)

    def bellman_ford(self, src, P):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(src, dist, P)