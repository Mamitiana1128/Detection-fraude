import tkinter as tk
from tkinter import messagebox
from collections import Counter

from graphe import construire_graphe, corriger_connexite, classification_sommets
from visualisation import afficher_graphe

def lancer_interface():

    fenetre = tk.Tk()

    fenetre.title("Détection de fraude")

    fenetre.geometry("600x500")

    graphe = None
    classes = None

    def generer():

        nonlocal graphe, classes

        try:

            n = int(entree_n.get())
            p = float(entree_p.get())

        except ValueError:

            messagebox.showerror(
                "Erreur",
                "Valeurs invalides"
            )

            return

        graphe = construire_graphe(n, p)

        graphe = corriger_connexite(graphe)

        classes = classification_sommets(graphe)

        nb_aretes = sum(len(v) for v in graphe) // 2

        compteur = Counter(classes)

        texte_stats.set(
            f"Nombre de sommets : {n}\n\n"
            f"Nombre d'arêtes : {nb_aretes}\n\n"
            f"Centraux : {compteur.get('Central',0)}\n"
            f"Intermédiaires : {compteur.get('Intermediaire',0)}\n"
            f"Périphériques : {compteur.get('Peripherique',0)}\n"
            f"Cliques : {compteur.get('Clique',0)}"
        )

    def afficher():

        if graphe is None:
            return

        if len(graphe) > 300:

            messagebox.showinfo(
                "Information",
                "Graphe trop grand pour une visualisation complète."
            )

            return

        afficher_graphe(graphe, classes)

    # ------------------------------------------------

    tk.Label(
        fenetre,
        text="Détection de fraude",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    cadre = tk.Frame(fenetre)

    cadre.pack()

    tk.Label(
        cadre,
        text="Nombre de sommets :"
    ).grid(row=0, column=0)

    entree_n = tk.Entry(cadre)

    entree_n.grid(row=0, column=1)

    tk.Label(
        cadre,
        text="Probabilité p :"
    ).grid(row=1, column=0)

    entree_p = tk.Entry(cadre)

    entree_p.grid(row=1, column=1)

    tk.Button(fenetre,text="Générer le graphe",command=generer).pack(pady=10)

    texte_stats = tk.StringVar()

    tk.Label(fenetre,textvariable=texte_stats,justify="left",font=("Consolas", 11)).pack(pady=15)

    tk.Button(fenetre,text="Afficher le graphe",command=afficher).pack()

    fenetre.mainloop()