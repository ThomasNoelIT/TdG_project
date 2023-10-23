import networkx as nx
import numpy as np
import sympy
import matplotlib.pyplot as plt

# Définition de la fonction pour calculer le polynôme chromatique
def chromatic_polynomial(graph, variable):
    # Obtenir le nombre de nœuds dans le graphe
    n = len(graph.nodes())

    # Calcul de la matrice d'adjacence du graphe
    adjacency_matrix = nx.adjacency_matrix(graph)

    # Conversion de la matrice d'adjacence en une matrice NumPy d'entiers
    adjacency_matrix = np.array(adjacency_matrix, dtype=int)

    # Calcul du polynôme chromatique en utilisant le déterminant de la matrice modifiée
    char_poly = np.linalg.det(adjacency_matrix - variable * np.identity(n))

    # Retourne le polynôme chromatique sous forme d'objet SymPy
    return sympy.Poly(char_poly)

# Création d'un graphe vide
G = nx.Graph()

# Définition des arêtes du graphe
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Ajout des arêtes au graphe
G.add_edges_from(edges)

# Calcul du polynôme chromatique du graphe
chromatic_polynomial = nx.chromatic_polynomial(G)

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


# nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=500, font_size=12)
# plt.show()

# # Variable symbolique pour le polynôme chromatique
# z = sympy.symbols('z')

# # Calcul du polynôme chromatique
# chromatic_poly = chromatic_polynomial(G, z)
# print(chromatic_poly)
