from os import read
import networkx as nx
import matplotlib.pyplot as plt
from prim import Prim
import numpy as np
# from djisktra import Dijkstra
# from floydwarshall import floydWarshall


f = open("input10.txt")
firstline = f.readline()

G = nx.Graph()             #normal Graph
P = nx.Graph()              #graph after applying algorithm

for i in range(0, int(firstline)):
    y = f.readline()
    y = y.split()
    node = [float(i) for i in y]
    vertice = node[0]
    x_cord = node[1]
    y_cord = node[2]
    print(vertice, x_cord, y_cord)
    G.add_node(vertice, pos = (x_cord, y_cord))
    P.add_node(vertice, pos = (x_cord, y_cord))

for i in range (0, int(firstline)):
    y = f.readline()
    y = y.split()
    edge = [float(i) for i in y]
    for j in range(1,len(edge),4):
        print(edge[0], edge[j], edge[j+2])
        
        if edge[0] != edge[j]:
            G.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)
            #P.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)
        
AdjMat = nx.to_numpy_matrix (G)
AdjList = AdjMat.tolist()


             #algorithm call
#Kruskal(G)
#Dijkstra(P,0,int(firstline))


pos = nx.get_node_attributes(G,'pos')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)       #labels = edges
plt.figure(1)
nx.draw(G, pos, with_labels = True)
#print(G)

Prim(AdjList,P,firstline)

#floydWarshall(P, firstline)

plt.show()