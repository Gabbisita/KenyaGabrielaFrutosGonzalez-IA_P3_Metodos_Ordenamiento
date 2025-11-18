def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivote = arr[len(arr) // 2]
    # Usando "list comprehension" para la partición
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    
    # Llamada recursiva
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"QuickSort: {quick_sort(lista.copy())}")