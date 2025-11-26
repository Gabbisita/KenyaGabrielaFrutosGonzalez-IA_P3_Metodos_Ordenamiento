import heapq
import matplotlib.pyplot as plt
import networkx as nx
import os 
# La librería time ya no es necesaria pues no usamos animación en tiempo real.

def prim_simulador_estatico(grafo_ciudades, pos_ciudades, inicio_ciudad):

    # 1. Preparación de la carpeta de salida
    output_dir = "pasos_prim"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Configuración Inicial del Grafo
    G_display = nx.Graph()
    for ciudad in grafo_ciudades:
        for vecino, coste in grafo_ciudades[ciudad]:
            # Añadimos la arista solo una vez
            if ciudad < vecino: 
                 G_display.add_edge(ciudad, vecino, weight=coste)
        if ciudad not in G_display.nodes():
             G_display.add_node(ciudad)

    # Función de Dibujo para Guardar la Imagen
    paso_contador = 0
    def dibujar_grafo(titulo, aem_actual_aristas, visitados_actual, aristas_candidatas_display, nuevo_borde=None):
        nonlocal paso_contador
        paso_contador += 1
        
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_title(titulo, fontsize=16)

        # Colores de nodos: verde (visitados), azul (inicio), celeste (restantes)
        node_colors = ['green' if node in visitados_actual else 'skyblue' for node in G_display.nodes()]
        if inicio_ciudad in visitados_actual:
             node_colors[list(G_display.nodes()).index(inicio_ciudad)] = 'blue'

        # Dibujar nodos y aristas base (gris claro)
        nx.draw_networkx_nodes(G_display, pos_ciudades, node_color=node_colors, node_size=1000, ax=ax)
        nx.draw_networkx_edges(G_display, pos_ciudades, edge_color='lightgray', width=1, ax=ax)
        
        # Etiquetas de peso de todas las aristas
        edge_labels_all = nx.get_edge_attributes(G_display, 'weight')
        nx.draw_networkx_edge_labels(G_display, pos_ciudades, edge_labels=edge_labels_all, font_color='gray', ax=ax)

        # Dibujar las aristas del AEM actual en ROJO
        aem_edges_tuple = [(u, v) for u, v, _ in aem_actual_aristas]
        nx.draw_networkx_edges(G_display, pos_ciudades, edgelist=aem_edges_tuple, edge_color='red', width=2, ax=ax)
        
        # Resaltar la última arista añadida en LIME VERDE
        if nuevo_borde:
            nx.draw_networkx_edges(G_display, pos_ciudades, edgelist=[nuevo_borde], edge_color='lime', width=3, style='dashed', ax=ax)

        # Resaltar aristas candidatas en NARANJA punteado
        candidatas_edges_tuple = [(o, d) for p, o, d in aristas_candidatas_display]
        nx.draw_networkx_edges(G_display, pos_ciudades, edgelist=candidatas_edges_tuple, edge_color='orange', width=1.5, style='dotted', ax=ax)

        # Etiquetas de nodos
        nx.draw_networkx_labels(G_display, pos_ciudades, font_size=12, font_weight='bold', ax=ax)
        
        # Guardar la imagen y cerrar la figura
        filename = os.path.join(output_dir, f"Paso_{paso_contador:02d}.jpg")
        plt.savefig(filename)
        plt.close(fig) 
        print(f"   -> Imagen guardada: {filename}")

    # Lógica del Algoritmo de Prim
    visitados = {inicio_ciudad} # Nodos ya en el AEM
    aristas_candidatas = []      # Cola de prioridad: (peso, origen, destino)
    aem = []                     # Aristas del AEM final
    coste_total = 0

    # Inicialización
    for vecino, peso in grafo_ciudades.get(inicio_ciudad, []):
        heapq.heappush(aristas_candidatas, (peso, inicio_ciudad, vecino))

    print("Inicio")
    print(f"Los pasos gráficos se guardarán en: {output_dir}")
    dibujar_grafo(f"Paso 0: Comienzo desde {inicio_ciudad}", [], visitados, aristas_candidatas)

    while aristas_candidatas and len(visitados) < len(grafo_ciudades):
        # 1. Selección de la arista de menor coste
        peso, origen, destino = heapq.heappop(aristas_candidatas)

        if destino not in visitados:
            # 2. Inclusión en el AEM
            visitados.add(destino)
            aem.append((origen, destino, peso))
            coste_total += peso
            
            print(f"\n[PASO] Arista seleccionada: ({origen} - {destino}) Coste: {peso}.")

            # Dibuja y guarda la imagen con la nueva arista
            dibujar_grafo(f"Paso {len(aem)}: Añadida ({origen}-{destino}). Coste Acumulado: {coste_total}", aem, visitados, aristas_candidatas, (origen, destino))

            # 3. Expansión de candidatas
            for vecino, nuevo_peso in grafo_ciudades.get(destino, []):
                if vecino not in visitados:
                    heapq.heappush(aristas_candidatas, (nuevo_peso, destino, vecino))
            
        else:
            # 4. Arista descartada por formar ciclo
            print(f"\n[DESCARTADO] Arista: ({origen} - {destino}). Crea un ciclo.")
            # Dibuja el estado, pero no se añade ninguna arista al AEM
            dibujar_grafo(f"Paso {len(aem)}: Descartada ({origen}-{destino}) (Ciclo)", aem, visitados, aristas_candidatas)


    #  Resultado Final
    print("\n Fin.")
    print("-" * 50)
    print("Árbol de Expansión Mínima (AEM) Final:")
    for o, d, p in aem:
        print(f"  - Carreta de {o} a {d} (Coste: {p})")
    print(f"Coste Total Final: {coste_total}")
    
    # Dibuja y guarda la imagen final
    dibujar_grafo(f"AEM Final. Coste Total: {coste_total}", aem, visitados, [])

# Ciudades y sus posibles conexiones con los costes
ciudades_y_carreteras = {
    'CDMX': [('Guadalajara', 400), ('Puebla', 150), ('Querétaro', 200)],
    'Guadalajara': [('CDMX', 400), ('Monterrey', 600), ('Puerto Vallarta', 250)],
    'Puebla': [('CDMX', 150), ('Oaxaca', 300), ('Veracruz', 180)],
    'Querétaro': [('CDMX', 200), ('San Luis Potosí', 220)],
    'Monterrey': [('Guadalajara', 600), ('San Luis Potosí', 380)],
    'Oaxaca': [('Puebla', 300), ('Tuxtla Gtz', 450)],
    'Veracruz': [('Puebla', 180), ('Villahermosa', 280)],
    'San Luis Potosí': [('Querétaro', 220), ('Monterrey', 380), ('Zacatecas', 190)],
    'Puerto Vallarta': [('Guadalajara', 250)],
    'Tuxtla Gtz': [('Oaxaca', 450), ('Villahermosa', 200)],
    'Villahermosa': [('Veracruz', 280), ('Tuxtla Gtz', 200)]
}

# Posiciones de las ciudades (Coordenadas completas y corregidas)
posiciones = {
    'CDMX': (-0.5, 0), 'Guadalajara': (-1.5, 0.5), 'Puebla': (0.5, -0.5),
    'Querétaro': (-0.8, 0.8), 'Monterrey': (-1.0, 1.5), 'Oaxaca': (0.8, -1.2),
    'Veracruz': (1.2, -0.2), 'San Luis Potosí': (-0.5, 1.2),
    'Puerto Vallarta': (-2.0, 0.0), 'Tuxtla Gtz': (1.5, -1.5),
    'Villahermosa': (2.0, -0.8), 'Zacatecas': (-1.5, 1.2) 
}

# Ejecutar
prim_simulador_estatico(ciudades_y_carreteras, posiciones, 'CDMX')