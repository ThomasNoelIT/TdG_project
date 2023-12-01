import networkx as nx
import numpy as np
#import numpy.polynomial.polynomial as nppol
import sympy as sp
import math
import matplotlib.pyplot as plt
#Un simple graphe non orienté ne contient ni arêtes en double ni boucles

# Définition de la fonction pour calculer le polynôme chromatique
def chromatic_polynomialT(graph, variable):
    n = len(graph.nodes())
    adjacency_matrix = nx.adjacency_matrix(graph).toarray()

    # Assurez-vous que la matrice d'adjacence est de type entier
    adjacency_matrix = np.asarray(adjacency_matrix, dtype=int)

    # Utilisez la bibliothèque SymPy pour le calcul du déterminant
    char_poly = sp.det(sp.Matrix(adjacency_matrix) - variable * sp.eye(n))

    # Retourne le polynôme chromatique sous forme d'objet SymPy
    return sp.Poly(char_poly)

# Fonction pour trouver le nombre de coloriages propres distincts du graphe
#def color_number():


# Fonction qui décrit la formule du polynôme chromatique
def c_p(x, long):
    if x == 0:
        poly = 0
    for i in long:
        for j in i:
            calcul = math.factorial(x-j)
        poly = (x//math.factorial(i)) * calcul
    return poly

# Fonction pour trouver les arêtes qui contiennent encore le sommet supprimé : souci ici car il faut remplacer
# le sommet supprimé par un de ses voisins
def find_in(remember, edges):
    list = []
    for i in range(len(edges)):
        (x, y) = edges[i]
        print("edges[i] =", edges[i])
        if (x == remember) or (y == remember):
            list.append((x, y))
    return list

# Fonction pour calculer le polynôme chromatique
def chromatic_polynomialR(G, edges):
    for i in range(len(edges)):
        (remember1, remember2) = edges[len(edges)-1]
        find_in(remember2, edges)

        G.remove_edge(remember1, remember2) #souci ici car G est une liste et non un graphe
        minus = list(G.edges)
        chPoly = chromatic_polynomialR(minus, edges)

    return chPoly

# Création d'un graphe vide
G = nx.Graph()

# Définition des arêtes du graphe par entrées
def edges(G):
    nombre = input('Combien d\'arêtes votre graphe contient-il ?\n')
    edges = []
    for i in range(1, int(nombre)+1):
        ajout = int(input('Premier sommet relié '+ str(i) + ': '))
        ajout2 = int(input('Second sommet relié '+ str(i) + ': '))
        # Vérifie que le graphe soit simple et non orienté
        if (ajout != ajout2) and ((ajout, ajout2) not in edges) and ((ajout2, ajout) not in edges):
            edges.append((ajout, ajout2))
            boolean = False
        else:
            boolean = True
            print("Votre proposition de graphe a un soucis, il ne respecte pas la consigne d'un graphe simple non orienté.\n")
            return 0

    if (len(edges) > 0) and (boolean == False):
        #edges = [(1,2),(2,3),(3,4), (4,5)]#, (5,6), (4,6), (6,7), (7,8), (8,9), (9,10), (10, 11), (11, 12), (12,13), (13,14), (14,15)]#, (15,16), (16,17), (17,18),(18,19),(19,20),(20,21),(21,1)]
        #graph = create_graph(edges)
        G.add_edges_from(edges)
    else:
        print("Le graphe est nul.\n")
        G.clear()

    graph = list(G.edges)
    return graph

# Ajout des arêtes au graphe
graph = edges(G)
#variable = sp.symbols('x')

#chromatic_polynomialR(G, graph)

if (len(graph) > 0):
    # Calcul du polynôme chromatique du graphe
    chromatic_polynomial = nx.chromatic_polynomial(G)
    #chromatic_polynomial = chromatic_polynomialT(G, variable)
    #chromatic_polynomial = chromatic_polynomialR(G, graph)

    # Génération d'une coloration du graphe avec la stratégie "largest_first"
    color_map = nx.coloring.greedy_color(G, strategy="largest_first")

    # Création d'une liste de couleurs pour chaque nœud en utilisant la coloration
    node_colors = [color_map[node] for node in G.nodes()]

    # Affichage du graphe avec des labels, des couleurs basées sur la coloration et d'autres paramètres graphiques
    nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.get_cmap('rainbow'), font_weight='bold', node_size=500, font_size=12)

    # Affichage du polynôme chromatique
    print("Polynôme chromatique:", chromatic_polynomial)

    # Affichage du graphe avec la coloration dans une fenêtre graphique
    plt.show()
