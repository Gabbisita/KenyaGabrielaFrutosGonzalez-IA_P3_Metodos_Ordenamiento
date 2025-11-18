# Hashing en acción (usando un diccionario)
# Python maneja el hash internamente

# Inserción (O(1) en promedio)
tabla_hash = {}
tabla_hash["manzana"] = 1
tabla_hash["banana"] = 2
tabla_hash["naranja"] = 3

# Búsqueda (O(1) en promedio)
print(f"Hashing (búsqueda): El valor de 'banana' es {tabla_hash['banana']}")

# Los elementos NO están ordenados
print(f"Contenido del Hash: {tabla_hash}")