
import argparse
import networkx as nx
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def contract_edge(graph, edge):
    u, v = edge
    # Créer un nouveau sommet représentant la contraction des sommets u et v
    new_vertex = max(max(edge) for edge in graph) + 1 if graph else 1
    
    # Mettre à jour les arêtes du graphe en contractant l'arête (u, v)
    new_edges = []
    for e in graph:
        if u in e or v in e:
            # Remplacer u et v par le nouveau sommet dans l'arête
            contracted_edge = tuple(new_vertex if x == u or x == v else x for x in e)
            new_edges.append(contracted_edge)
        else:
            new_edges.append(e)
    
    # Supprimer les boucles créées lors de la contraction
    new_edges = [e for e in new_edges if e[0] != e[1]]
    
    return new_edges

def remove_edge(edges, edge_to_remove):
    # Supprimer l'arête (u, v) du graphe
    edges = [e for e in edges if e != edge_to_remove]
    return edges


# def poly_chroma(edges, degree):
#     # Cas de base: si G est un graphe vide, le polynôme chromatique est 1
#     if degree < 1:
#         # print("chroma : "+str(chroma))
#         return [1]
    
#     chroma = [0] * (degree+1)
#     chroma[-1] = 1
#     # print(len(chroma))
#     print("chroma : "+str(chroma))
    
#     for e in edges:
#         # Supprimer l'arête e
#         without_edge = remove_edge(edges, e)
#         print("degree : "+str(degree))
#         print("without_edge : "+str(without_edge))
#         # Calculer le polynôme chromatique du graphe sans l'arête e
#         poly_without_edge = poly_chroma(without_edge, degree - 1)
        
#         # Contracter l'arête e
#         contracted_edge = contract_edge(edges, e)
#         # Calculer le polynôme chromatique du graphe contracté
#         poly_contracted = poly_chroma(contracted_edge, degree - 1)

#         chroma = np.add(chroma, np.subtract(poly_without_edge, poly_contracted))
        
#     return chroma

def poly_chroma(edges, degree):
    # Cas de base: si G est un graphe vide, le polynôme chromatique est 1
    if degree < 1:
        return [1]

    chroma = [0] * (degree + 1)
    chroma[-1] = 1

    for e in edges:
        # Supprimer l'arête e
        without_edge = remove_edge(edges, e)

        # Calculer le polynôme chromatique du graphe sans l'arête e
        poly_without_edge = poly_chroma(without_edge, degree - 1)

        # Contracter l'arête e
        contracted_edge = contract_edge(edges, e)

        # Calculer le polynôme chromatique du graphe contracté
        poly_contracted = poly_chroma(contracted_edge, degree - 1)

        # Mettre à jour le polynôme chromatique en soustrayant et ajoutant les polynômes calculés
        chroma = [x + y for x, y in zip(chroma, [a - b for a, b in zip(poly_without_edge, poly_contracted)])]

    return chroma






def main(edges):
    # Convertir la chaîne d'arêtes en une liste d'arêtes
    # edges_list = [tuple(map(int, edge.strip('()').split(','))) for edge in edges_str.split('),(')]
    print(edges)
    
    # Utilisez la fonction max avec une clé personnalisée pour extraire le tuple avec la valeur maximale
    max_tuple = max(edges, key=lambda x: max(x))

    # Utilisez ensuite la fonction max pour extraire la valeur maximale du tuple résultant
    poly_chroma_degree = max(max_tuple)

    # Calculer le polynôme chromatique
    result = poly_chroma(edges, poly_chroma_degree)
    
    print("Polynôme chromatique:", result)
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcul du polynôme chromatique et affichage du graphe avec coloration.")
    parser.add_argument("edges", type=str, help="Liste des arêtes du graphe sous la forme '(1, 2),(3, 1),(2, 3), (3, 1), (3, 4)'")
    args = parser.parse_args()
    edges = eval(args.edges)
    main(edges)




