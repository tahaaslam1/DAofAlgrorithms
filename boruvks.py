from queue import PriorityQueue
from os import read
import networkx as nx
import matplotlib.pyplot as plt

class Boruvka:
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
                    g.addEdge(int(edge[0]), int(edge[j]), float(edge[j+2]/10000000))


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

        g.boruvkaMST(P)

        plt.show()

class Graph: 
# These are the four small functions used in main Boruvkas function
     # It does union of two sets of x and y with the help of rank
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
        if rank[xroot] < rank[yroot]:  
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot #Make one as root and increment.
            rank[xroot] += 1

    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] # default dictionary


    # add an edge to the graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # find set of an element i 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

   
#***********************************************************************
    #constructing MST
    def boruvkaMST(self, P): 
        parent = [];
        rank = []; 
        cheapest =[]      
        numTrees = self.V 
        MSTweight = 0     
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
            cheapest =[-1] * self.V 

        # Keep combining components (or sets) until all 
        # compnentes are not combined into single MST 

        while numTrees > 1: 
            for i in range(len(self.graph)): 

                u,v,w = self.graph[i] 
                set1 = self.find(parent, u) 
                set2 = self.find(parent ,v) 

               
                if set1 != set2:   

                    if cheapest[set1] == -1 or cheapest[set1][2] > w : 
                        cheapest[set1] = [u,v,w] 

                    if cheapest[set2] == -1 or cheapest[set2][2] > w : 
                        cheapest[set2] = [u,v,w] 

            # Consider the above picked cheapest edges and add them to MST 
            for node in range(self.V): 
                if cheapest[node] != -1: 
                    u,v,w = cheapest[node] 
                    set1 = self.find(parent, u) 
                    set2 = self.find(parent ,v) 

                    if set1 != set2 : 
                        MSTweight += w 
                        self.union(parent, rank, set1, set2) 
                        print ("Edge %d-%d has weight %d is included in MST" % (u,v,w)) 
                        P.add_edge(u,v, weight = w)
                        numTrees = numTrees - 1

             
            cheapest =[-1] * self.V 


        pos = nx.get_node_attributes(P,'pos')
        labels = nx.get_edge_attributes(P,'weight')
        print(labels)
        nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
        plt.figure(2)
        nx.draw(P, pos, with_labels = True) 

        print(P)