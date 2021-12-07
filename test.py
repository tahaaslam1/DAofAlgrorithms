from os import read
import networkx as nx
import matplotlib.pyplot as plt

f = open("input10.txt")
x = f.readline()

G = nx.Graph()
PrimsGraph = nx.Graph()

f.readline()
for i in range(0,int(x)):
    y = f.readline()
    y = y.split()
    node = [float(i) for i in y]
    G.add_node(node[0] , pos=(node[1] , node[2]))

f.readline()

for i in range (0 , int(x)):
    y = f.readline()
    y = y.split()
    edge = [float(i) for i in y]
    for j in range(1,len(edge),4):
        if(edge[0] != edge[j]):
            G.add_edge(edge[0] , edge[j] , weight=edge[j+2]/10000000)
        

pos = nx.get_node_attributes(G,'pos')
labels = nx.get_edge_attributes(G,'weight')

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw(G, pos, with_labels = True)

AdjMatrix = nx.to_numpy_matrix(G)

AdjList = AdjMatrix.tolist()

   
plt.draw()
plt.show()