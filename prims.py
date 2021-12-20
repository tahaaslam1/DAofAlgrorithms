from queue import PriorityQueue
from os import read
import networkx as nx
import matplotlib.pyplot as plt

class Prims:
    def __init__(self, file):
        self.f = open(file)

    def show(self):
        firstline = self.f.readline()

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
                G.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)

        print(G)    
        AdjMat = nx.to_numpy_matrix (G)
        AdjList = AdjMat.tolist()
        pos = nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)       
        plt.figure(1)
        nx.draw(G, pos, with_labels = True)

        Prim(AdjList,P,firstline)

        plt.show()

def Prim(AdjList,P,firstline):
 INF = -9999999
 V = int(firstline)    
 selected = [0] * V    
 no_edge = 0        

 selected[0] = True
 print("Edge : Weight\n")
 while (no_edge < V - 1):
    maximum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and AdjList[i][j]):   
                    if maximum < AdjList[i][j]:     
                        maximum = AdjList[i][j]     
                        x = i
                        y = j
    P.add_edge(x, y, weight = float(AdjList[x][y])) 
    print(str(x) + "-" + str(y) + ": " + str(AdjList[x][y]))    
    selected[y] = True
    no_edge += 1

    pos = nx.get_node_attributes(P,'pos')
    labels = nx.get_edge_attributes(P,'weight')
    nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
    plt.figure(2)
    nx.draw(P, pos, with_labels = True)