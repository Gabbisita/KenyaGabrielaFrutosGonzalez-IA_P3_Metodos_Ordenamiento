import bisect

def binary_insertion_sort(arr):
  for i in range(1, len(arr)):
    elemento_a_insertar = arr[i]
    
    # 1. Encontrar la posición usando búsqueda binaria
    posicion = bisect.bisect_left(arr, elemento_a_insertar, 0, i)
    
    # 2. Desplazar e insertar
    # Opción simple: re-insertar el elemento
    arr.pop(i)
    arr.insert(posicion, elemento_a_insertar)
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Inserción Binaria: {binary_insertion_sort(lista.copy())}")