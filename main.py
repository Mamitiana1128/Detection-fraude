import random
from collections import deque

# Construction du graphe

def construire_graphe(n, p):

    # On initialise une liste d'adjacence vide pour chaque sommet
    adj = [[] for k in range(n)]

    for i in range(n - 1):

        for j in range(i + 1, n):

            # On tire au sort : si r < p, on ajoute l'arete
            if random.random() < p:

                adj[i].append(j)
                adj[j].append(i)

    return adj

# Correction du connexité
def corriger_connexite(adj):

    n = len(adj)
    visite = [False] * n
    visites_globales = []

    for premier_sommet in range(n):

        if not visite[premier_sommet]:

            if visites_globales:

                u = random.choice(visites_globales)
                adj[u].append(premier_sommet)
                adj[premier_sommet].append(u)

            file = deque([premier_sommet])
            visite[premier_sommet] = True


            while file:

                u = file.popleft()
                visites_globales.append(u)

                for v in adj[u]:

                    if not visite[v]:

                        visite[v] = True
                        file.append(v)
    return adj


# Detection des cliques

def detection_cliques(adj):

    cliques = []

    for v in range(len(adj)):

        voisins = adj[v]

        if len(voisins) < 2:
            continue

        liens = 0
        total = len(voisins) * (len(voisins) - 1)

        for i in voisins:

            for j in voisins:

                if i != j and j in adj[i]:
                    liens += 1

        if total > 0:

            densite = liens / total

            if densite > 0.6:

                cliques.append(v)

    return cliques


# Classification

def classification_sommets(adj):

    def detection_cliques(adj):

        cliques = []
        for v in range(len(adj)):

            voisins = adj[v]
            if len(voisins) < 2:
                continue

            liens = 0
            total = len(voisins) * (len(voisins) - 1)

            for i in voisins:

                for j in voisins:

                    if i != j and j in adj[i]:

                        liens += 1

            if total > 0:

                densite = liens / total

                if densite > 0.6:

                    cliques.append(v)

        return cliques

    degres = [len(v) for v in adj]
    moyenne = sum(degres) / len(degres)

    cliques = detection_cliques(adj)

    classes = []

    for v in range(len(adj)):

        if v in cliques:

            classes.append("Clique")

        elif degres[v] > moyenne:

            classes.append("Central")

        elif degres[v] >= moyenne - 1 :

            classes.append("Intermediaire")

        else:

            classes.append("Peripherique")

    return classes


# Affichage du resultat

def affichage_resultat(graphe , classes ) :

    print("\nClassification des sommets : ")

    for sommet, classe in enumerate(classes) :

        print(f"Sommet {sommet} : {classe}")



# Programme Principal

if __name__ == "__main__":

    n = int(input("Nombre de sommets : "))
    p = float(input("Probabilite : "))

    graphe = construire_graphe(n, p)
    graphe = corriger_connexite(graphe)
    classes = classification_sommets(graphe)
    affichage_resultat(graphe , classes )
