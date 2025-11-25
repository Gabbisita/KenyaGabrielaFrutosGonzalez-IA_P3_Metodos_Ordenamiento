import collections
import networkx as nx
import matplotlib.pyplot as plt

#1. Clase Union-Find
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return True
        return False

#2. Algoritmo de Kruskal
def kruskal(vertices, aristas):
    """
    Simulador del Algoritmo de Kruskal paso a paso y visualización final.
    """
    aristas_ordenadas = sorted(aristas, key=lambda item: item[2])
    uf = UnionFind(vertices)
    aem = []
    coste_total = 0
    
    print("Simulador Algoritmo de Kruskal")
    
    for u, v, w in aristas_ordenadas:
        root_u = uf.find(u)
        root_v = uf.find(v)

        if root_u != root_v:
            uf.union(u, v)
            aem.append((u, v, w))
            coste_total += w
        
        if len(aem) == len(vertices) - 1:
            break

    # 4. Resultado Final
    print("RESULTADO FINAL (Árbol de Expansión Mínima)")
    print(f"COSTO MÍNIMO TOTAL: {coste_total}")
    
    # 5. Visualización Gráfica
    visualizar_mst(vertices, aristas, aem, coste_total)


def visualizar_mst(vertices, todas_aristas, aem, coste_total):
    """
    Crea un gráfico usando NetworkX y Matplotlib.
    """
    G = nx.Graph()
    
    # 1. Agregar todos los nodos
    G.add_nodes_from(vertices)

    # 2. Agregar todas las aristas con sus pesos originales para el contexto
    # Mapeo de pesos para NetworkX
    edge_labels = {}
    for u, v, w in todas_aristas:
        G.add_edge(u, v, weight=w)
        edge_labels[(u, v)] = w

    # 3. Definir la posición de los nodos (layout)
    pos = nx.spring_layout(G, seed=42) # Usar una semilla para resultados reproducibles

    plt.figure(figsize=(10, 7))
    plt.title(f"Árbol de Expansión Mínima (Kruskal) | Coste Total: {coste_total}", fontsize=14)

    # 4. Dibujar TODAS las aristas
    # Las que SÍ están en el AEM (verde, más gruesas)
    aem_aristas_simple = [(u, v) for u, v, w in aem]
    nx.draw_networkx_edges(
        G, pos, 
        edgelist=aem_aristas_simple, 
        width=3, 
        alpha=0.8, 
        edge_color='g', 
        label="AEM (Seleccionadas)"
    )
    
    # Las que no están en el AEM (rojo, más finas y transparentes)
    todas_aristas_simple = [(u, v) for u, v, w in todas_aristas]
    aristas_descartadas = [e for e in todas_aristas_simple if e not in aem_aristas_simple and (e[1], e[0]) not in aem_aristas_simple]
    nx.draw_networkx_edges(
        G, pos, 
        edgelist=aristas_descartadas, 
        width=1, 
        alpha=0.4, 
        edge_color='r', 
        style='dashed',
        label="Descartadas"
    )

    # 5. Dibujar nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    
    # 6. Dibujar las etiquetas de peso en las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=10)

    # 7. Mostrar la leyenda y guardar
    plt.legend(handles=[plt.Line2D([0], [0], color='g', lw=4), plt.Line2D([0], [0], color='r', lw=2, linestyle='--')], 
               labels=['Aristas del AEM', 'Aristas Descartadas'])
    plt.axis('off') # Ocultar los ejes
    
    # Guarda el archivo de imagen
    nombre_archivo = "kruskal_mst_visualizacion.png"
    plt.savefig(nombre_archivo) 
    print(f"\n Se ha generado la visualización gráfica en el archivo: **{nombre_archivo}**")
    print("Búscalo en el directorio donde ejecutaste el script.")
    plt.close() # Cierra la figura de Matplotlib

# Datos de prueba
vertices = {'A', 'B', 'C', 'D', 'E'} 
aristas = [
    ('A', 'B', 10), ('A', 'C', 6), ('B', 'C', 4),
    ('B', 'D', 12), ('C', 'E', 7), ('D', 'E', 9),
    ('C', 'D', 8)
]

kruskal(vertices, aristas)