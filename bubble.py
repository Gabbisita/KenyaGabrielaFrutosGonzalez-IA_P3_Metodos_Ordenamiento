def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    # Bandera para optimizar: si no hay intercambios, está ordenado
    swapped = False
    for j in range(0, n - i - 1):
      # Compara elementos adyacentes
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j] # Intercambio
        swapped = True
    if not swapped:
      break
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Burbuja: {bubble_sort(lista.copy())}")