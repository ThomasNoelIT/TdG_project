import networkx as nx
import numpy as np
import sympy
import matplotlib.pyplot as plt

def chromatic_polynomial(graph, variable):
    n = len(graph.nodes())
    adjacency_matrix = nx.adjacency_matrix(graph)
    adjacency_matrix = np.array(adjacency_matrix, dtype=int)  # Convertir en une matrice NumPy d'entiers
    char_poly = np.linalg.det(adjacency_matrix - variable * np.identity(n))
    return sympy.Poly(char_poly)

# Créer un graphe simple
G = nx.Graph()
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]
G.add_edges_from(edges)

chromatic_polynomial = nx.chromatic_polynomial(G)

# Afficher le graphe avec une coloration basée sur le polynôme chromatique
color_map = nx.coloring.greedy_color(G, strategy="largest_first")
node_colors = [color_map[node] for node in G.nodes()]

nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.get_cmap('rainbow'), font_weight='bold', node_size=500, font_size=12)

# Afficher le polynôme chromatique
print("Polynôme chromatique:", chromatic_polynomial)

# Afficher le graphe
plt.show()

# nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=500, font_size=12)
# plt.show()

# # Variable symbolique pour le polynôme chromatique
# z = sympy.symbols('z')

# # Calcul du polynôme chromatique
# chromatic_poly = chromatic_polynomial(G, z)
# print(chromatic_poly)
