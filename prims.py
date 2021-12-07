import networkx as nx
import matplotlib.pyplot as plt
def Prim(AdjList,P,firstline):
 INF = 9999999
 V = int(firstline)    #
 selected = [0] * V     #
 no_edge = 0        

 selected[0] = True
 print("Edge : Weight\n")
 while (no_edge < V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and AdjList[i][j]):   #
                    if minimum > AdjList[i][j]:     #
                        minimum = AdjList[i][j]     #
                        x = i
                        y = j
    P.add_edge(x, y, weight = float(AdjList[x][y])) #
    print(str(x) + "-" + str(y) + ": " + str(AdjList[x][y]))    #
    selected[y] = True
    no_edge += 1

    pos = nx.get_node_attributes(P,'pos')
    labels = nx.get_edge_attributes(P,'weight')
    nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
    plt.figure(2)
    nx.draw(P, pos, with_labels = True)