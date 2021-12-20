from queue import PriorityQueue
from os import read
import networkx as nx
import matplotlib.pyplot as plt

class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addedge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, father, i):
        if father[i] == i:
            return i
        return self.find(father, father[i])

    def apply_union(self, father, rank, x, y):
        x = self.find(father, x)
        y = self.find(father, y)
        if rank[x] < rank[y]:
            father[x] = y
        elif rank[x] > rank[y]:
            father[y] = x
        else:
            father[y] = x
            rank[x] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self, P):
        res = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        father = []
        rank = []
        for vertex in range(self.V):
            father.append(vertex)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(father, u)
            y = self.find(father, v)
            if x != y:
                e = e + 1
                res.append([u, v, w])
                self.apply_union(father, rank, x, y)
        for u, v, weight in res:
            print("%d - %d: %d" % (u, v, weight))
            P.add_edge(u, v, weight=weight)

        pos = nx.get_node_attributes(P,'pos')
        labels = nx.get_edge_attributes(P,'weight')
        print(labels)
        nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
        plt.figure(2)
        nx.draw(P, pos, with_labels = True)
        
        print(P)

class Kruskal:
    def __init__(self, file):
        self.f = open(file)

    def show(self):    
        linee = self.f.readline()

        g = KruskalGraph(int(linee))
        G = nx.Graph()             #normal Graph
        P = nx.Graph()              #graph after applying algorithm

        for i in range(0, int(linee)):
            y = self.f.readline()
            y = y.split()
            vertex = [float(i) for i in y]
            vertice = vertex[0]
            x_cordinate = vertex[1]
            y_cordinate = vertex[2]
            print(vertice, x_cordinate, y_cordinate)
            G.add_node(vertice, pos = (x_cordinate, y_cordinate))
            P.add_node(vertice, pos = (x_cordinate, y_cordinate))

        for i in range (0, int(linee)):
            y = self.f.readline()
            y = y.split()
            lakeer = [float(i) for i in y]
            for j in range(1,len(lakeer),4):
                print(lakeer[0], lakeer[j], lakeer[j+2])
                
                if lakeer[0] != lakeer[j]:
                    G.add_edge(lakeer[0], lakeer[j], weight=lakeer[j+2]/10000000)
                    g.addedge(int(lakeer[0]), int(lakeer[j]), float(lakeer[j+2]/10000000))

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
        
        print("yahan")
        g.kruskal_algo(P)

        plt.show()


