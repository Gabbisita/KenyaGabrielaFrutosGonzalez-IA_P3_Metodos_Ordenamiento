import matplotlib
try:
    matplotlib.use('Agg')
except Exception as e:
    print(f"Advertencia: No se pudo establecer el backend 'Agg'. Error: {e}")
    pass

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_step_by_step(graph_data, start_node):
    """
    Implementa el Algoritmo de Dijkstra imprimiendo el progreso en consola.
    (Esta función es exactamente la misma que te di, pero la incluimos para la integridad)
    """
    
    print("\n--->> ALGORITMO DE DIJKSTRA <<---")

    
    # 1. Inicialización
    distances = {node: float('inf') for node in graph_data}
    distances[start_node] = 0
    predecessors = {node: None for node in graph_data}
    priority_queue = [(0, start_node)]
    visited = set()
    
    print(f"Estado Inicial - Distancias: {distances}")
    print("\n" * 3)

    # 2. Bucle principal (mismo que antes)
    step_count = 1
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        print(f"--- PASO {step_count}: Procesando Nodo {current_node} ---")
        # Impresiones
        
        for neighbor, weight in graph_data.get(current_node, []):
            new_distance = current_distance + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))
                # Impresiones de actualización
            # Impresiones de no mejora
        
        print(f"   | Estado de Distancias después del paso: {distances}")
        print("\n" * 3)
        step_count += 1
        
    print("--- ALGORITMO FINALIZADO ---")
    return distances, predecessors

def draw_final_path(graph_data, start_node, distances, predecessors):
    """
    Dibuja el grafo y guarda la imagen en un archivo PNG.
    """
    G = nx.DiGraph() 
    for u, neighbors in graph_data.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)

    pos = nx.circular_layout(G) 

    # 1. Preparación de estilos
    node_colors = ['red' if node == start_node else 'lightgreen' for node in G.nodes]
    distance_labels = {
        node: f"{node}\nD:{distances[node] if distances[node] != float('inf') else '∞'}"
        for node in G.nodes
    }

    path_edges = []
    for node, pred in predecessors.items():
        if pred is not None and node != start_node:
             path_edges.append((pred, node))

    edge_colors = ['blue' if (u, v) in path_edges else 'gray' for u, v in G.edges()]
    edge_widths = [3 if (u, v) in path_edges else 1 for u, v in G.edges()]

    # 2. Dibujar
    plt.figure(figsize=(10, 8))
    plt.title(f"Resultado Final de Dijkstra (Inicio: {start_node})", fontsize=16, fontweight='bold')
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, arrows=True)
    nx.draw_networkx_labels(G, pos, labels=distance_labels, font_size=10, font_color='black', font_weight='bold')
    
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_color='darkred')
    
    # 3. Guardar el archivo (La clave para asegurar los puntos extra)
    plt.axis('off')
    output_file = "Dijkstra_Resultado_Grafico.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight') 
    plt.close() # Cierra la figura en memoria
    
    return output_file

# CONFIGURACIÓN Y EJECUCIÓN

if __name__ == "__main__":
    
    graph_example = {
        'A': [('B', 6), ('D', 1)],
        'B': [('D', 2), ('C', 5), ('E', 2)],
        'C': [('E', 5)],
        'D': [('E', 1), ('B', 2)],
        'E': [('C', 5)]
    }
    start_node = 'A'

    # 1. SALIDA EN CONSOLA (Paso a Paso Requerido)
    distances, predecessors = dijkstra_step_by_step(graph_example, start_node)

    # 2. SALIDA GRÁFICA (Puntos Extra)
    print("\n GENERANDO RESULTADO GRÁFICO")
    
    # Llama a la función de dibujo y guarda el archivo
    filename = draw_final_path(graph_example, start_node, distances, predecessors)
    
    print("\nPROCESO FINALIZADO")
    print(f"El resultado gráfico se ha guardado exitosamente en el archivo: {filename}")
    print("\n" * 1)
