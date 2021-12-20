from tkinter import *
from check_prims import Prims
from check_djisktra import Djikstra
from check_floyd import Floyd
from check_boru import Boruvka
from check_cc import CC
from check_bellman import Bellman
from check_kruskal import Kruskal

window = Tk()
window.title('Design and analysis algorithm')
window.geometry("626x469")

bg = PhotoImage( file = "brick-wall-realistic_1284-4683.png")

clickedAlgo = StringVar()
clickedNodes = StringVar()

# Show image using label
label1 = Label( window, image = bg)
label1.place(x = 0,y = 0)

def prims() :
    p = Prims(f'input{clickedNodes.get()}filing.txt')
    p.show()

def djikstra():
    p = Djikstra(f'input{clickedNodes.get()}filing.txt')
    p.show()

def floyd():
    P = Floyd(f'input{clickedNodes.get()}filing.txt')
    P.show()

def boru():
    P = Boruvka(f'input{clickedNodes.get()}filing.txt')
    P.show()

def ClusteringCoefficient():
    P = CC(f'input{clickedNodes.get()}filing.txt')
    P.show()

def bellman():
    P = Bellman(f'input{clickedNodes.get()}filing.txt')
    P.show()

def kruskal():
    P = Kruskal(f'input{clickedNodes.get()}filing.txt')
    P.show()

def selected():
    myLabel = Label(window, text=clickedAlgo.get()).pack()

    if clickedAlgo.get() == "Prim's Algorithm":
        prims()

    if clickedAlgo.get() == "Dijkstra Algorithm":
        djikstra()

    if clickedAlgo.get() == "Floyd Warshall Algorithm":
        floyd()

    if clickedAlgo.get() == "Boruvkas Algorithm":
        boru()
    if clickedAlgo.get() == "Clustering Coefficient":
        ClusteringCoefficient()
        
    if clickedAlgo.get() == "Bellman Ford":
        bellman()

    if clickedAlgo.get() == "Kruskal Algorithm":
        kruskal()
    

option = [
    "Prim's Algorithm",
    "Kruskal Algorithm",
    "Dijkstra Algorithm",
    "Bellman Ford",
    "Floyd Warshall Algorithm",
    "Clustering Coefficient",
    "Boruvkas Algorithm",
]

nodes = [
    "10",
    "20",
    "30",
    "40",
    "50",
    "60",
    "70",
    "80",
    "90",
    "100"
]

value_inside = StringVar(window)
clickedAlgo.set("Select Algorithm")
drop = OptionMenu(window,clickedAlgo, *option)
drop.pack(pady= 20)

value_inside = StringVar(window)
clickedNodes.set("Select Number of Nodes")
drop = OptionMenu(window,clickedNodes, *nodes)
drop.pack(pady= 20)

myButton = Button(window, text = "Submit", command = selected)
myButton.pack()

window.mainloop()