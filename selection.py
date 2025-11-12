def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    # Encontrar el índice del mínimo elemento restante
    indice_minimo = i
    for j in range(i + 1, n):
      if arr[j] < arr[indice_minimo]:
        indice_minimo = j
        
    # Intercambiar el mínimo encontrado con el primer
    # elemento de la parte desordenada
    arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Selección: {selection_sort(lista.copy())}")