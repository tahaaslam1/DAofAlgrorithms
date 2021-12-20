from queue import PriorityQueue
from os import read
import networkx as nx
import matplotlib.pyplot as plt

INF = 999999

def floydWarshall(AdjList,firstline,P):
    nV = int(firstline)
    for i in range(nV):
        for j in range(nV):
            if (i == j):
                AdjList[i][j] = 0

            elif(AdjList[i][j] == 0):
                AdjList[i][j] = INF

    distance = list(map(lambda i: list(map(lambda j: j, i)), AdjList))
   
    
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = round(min(distance[i][j], distance[i][k] + distance[k][j]),2)
    print_solution(distance,nV,P)


# Printing the solution
def print_solution(distance,nV,P):
    print(distance)
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

    for i in range(nV):
        for j in range(nV):
            P.add_edge(i, j, weight=distance[i][j])
    
    pos = nx.get_node_attributes(P,'pos')
    labels = nx.get_edge_attributes(P,'weight')
    print(labels)
    nx.draw_networkx_edge_labels(P,pos,edge_labels=labels)
    plt.figure(2)
    nx.draw(P, pos, with_labels = True)
    print(P)