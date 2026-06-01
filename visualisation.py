import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def afficher_graphe(adj, classes):

    G = nx.Graph()

    for u in range(len(adj)):

        G.add_node(u)

        for v in adj[u]:
            if u < v:
                G.add_edge(u, v)

    couleurs = []

    for c in classes:

        if c == "Central":
            couleurs.append("red")

        elif c == "Clique":
            couleurs.append("yellow")

        elif c == "Peripherique":
            couleurs.append("green")

        else:
            couleurs.append("blue")

    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(G)

    nx.draw(G,pos,node_color=couleurs,with_labels=True,node_size=500
    )

    plt.title("Classification des sommets")

    legende = [
    Line2D([0], [0], marker='o', color='w',
            label='Central',
            markerfacecolor='red',
            markersize=10),

    Line2D([0], [0], marker='o', color='w',
            label='Intermediaire',
            markerfacecolor='blue',
            markersize=10),

    Line2D([0], [0], marker='o', color='w',
            label='Peripherique',
            markerfacecolor='green',
            markersize=10),

    Line2D([0], [0], marker='o', color='w',
            label='Clique',
            markerfacecolor='yellow',
            markersize=10)
    ]

    plt.legend(handles=legende, loc='best')

    plt.show()