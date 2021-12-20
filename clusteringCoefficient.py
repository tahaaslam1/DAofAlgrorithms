from os import read
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class CC:
    def __init__ (self, file):
        self.f = open(file)
    
    def show(self):
        firstline = self.f.readline()
        cc = 0

        G = nx.Graph()

        for i in range(0, int(firstline)):
            y = self.f.readline()
            y = y.split()
            node = [float(i) for i in y]
            vertice = node[0]
            x_cord = node[1]
            y_cord = node[2]
            print(vertice, x_cord, y_cord)
            G.add_node(vertice, pos = (x_cord, y_cord))

        for i in range (0, int(firstline)):
            y = self.f.readline()
            y = y.split()
            edge = [float(i) for i in y]
            for j in range(1,len(edge),4):
                print(edge[0], edge[j], edge[j+2])
                
                if edge[0] != edge[j]:
                    G.add_edge(edge[0], edge[j], weight=edge[j+2]/10000000)
                
        print("\n")

        A = nx.clustering(G)
        new_list = list(A.items())
        new_list = list(np.around(np.array(new_list),2))

        for i in range(0, int(firstline)):
            print("Clustering Coefficient for node ", i, " is: ", new_list[i][1])

        for i in range(0,int(firstline),1):
                cc = cc + new_list[i][1]

        avg_cc = cc / int(firstline)
        print("\nAverage CC is : " , "%.2f" % avg_cc)

        if(avg_cc >0.5 and avg_cc <= 1.0): 
            print('\nNeighbourhood is fully connected')               

        elif(avg_cc >= 0.0 and avg_cc < 0.5 ) : 
            print('\nLess connections in neighbourhood')

        elif(avg_cc == 0.5): 
            print("\nAverage Connections")

        pos = nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)       
        plt.figure(1)
        nx.draw(G, pos, with_labels = True)

        plt.show()