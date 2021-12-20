from os import read
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Floyd:
    def __init__(self, file):
        self.f = open(file)

    def show(self):    
        line = self.f.readline()

        G = nx.Graph()             #normal Graph
        P = nx.Graph()              #graph after applying algorithm

        for i in range(0, int(line)):
            y = self.f.readline()
            y = y.split()
            vertex = [float(i) for i in y]
            vertice = vertex[0]
            x_cordinate = vertex[1]
            y_cordinate = vertex[2]
            print(vertice, x_cordinate, y_cordinate)
            G.add_node(vertice, pos = (x_cordinate, y_cordinate))
            P.add_node(vertice, pos = (x_cordinate, y_cordinate))

        for i in range (0, int(line)):
            y = self.f.readline()
            y = y.split()
            lakeer = [float(i) for i in y]
            for j in range(1,len(lakeer),4):
                print(lakeer[0], lakeer[j], lakeer[j+2])
                
                if lakeer[0] != lakeer[j]:
                    G.add_edge(lakeer[0], lakeer[j], weight=lakeer[j+2]/10000000)
                    #P.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)
                
        AdjMat = nx.to_numpy_matrix (G)
        AdjList = AdjMat.tolist()

        pos = nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)       #labels = edges
        plt.figure(1)
        nx.draw(G, pos, with_labels = True)

        pos = nx.get_node_attributes(P,'pos')
        labels = nx.get_edge_attributes(P,'weight')
        print(labels)
        nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
        plt.figure(2)
        nx.draw(P, pos, with_labels = True)

        floydWarshall(AdjList,line,P)

        plt.show()

INF = 999999

def floydWarshall(AdjList,line,P):
    envy = int(line)
    for i in range(envy):
        for j in range(envy):
            if (i == j):
                AdjList[i][j] = 0

            elif(AdjList[i][j] == 0):
                AdjList[i][j] = INF

    dist = list(map(lambda i: list(map(lambda j: j, i)), AdjList))
   
    
    for k in range(envy):
        for i in range(envy):
            for j in range(envy):
                dist[i][j] = round(min(dist[i][j], dist[i][k] + dist[k][j]),2)
    print_solution(dist,envy,P)


# Printing the solution
def print_solution(dist,envy,P):
    print(dist)
    for i in range(envy):
        for j in range(envy):
            if(dist[i][j] == INF):
                print("INF", end=" ")
            else:
                print(dist[i][j], end="  ")
        print(" ")

    for i in range(envy):
        for j in range(envy):
            P.add_edge(i, j, weight=dist[i][j])
    
    pos = nx.get_node_attributes(P,'pos')
    labels = nx.get_edge_attributes(P,'weight')
    print(labels)
    nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
    plt.figure(2)
    nx.draw(P, pos, with_labels = True)
    print(P)