def insertion_sort(arr):
  # Empezamos desde el segundo elemento (índice 1)
  for i in range(1, len(arr)):
    elemento_a_insertar = arr[i]
    j = i - 1
    
    # Mover elementos de arr[0..i-1] que son
    # mayores que elemento_a_insertar, una posición a la derecha
    while j >= 0 and elemento_a_insertar < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    # Insertar el elemento en su posición correcta
    arr[j + 1] = elemento_a_insertar
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Inserción: {insertion_sort(lista.copy())}")