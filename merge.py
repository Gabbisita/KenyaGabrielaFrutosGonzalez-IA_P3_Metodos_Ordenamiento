def merge_sort(arr):
  if len(arr) > 1:
    # 1. Dividir
    medio = len(arr) // 2
    mitad_izquierda = arr[:medio]
    mitad_derecha = arr[medio:]
    
    # Llamada recursiva para cada mitad
    merge_sort(mitad_izquierda)
    merge_sort(mitad_derecha)
    
    # 2. Fusionar (Merge)
    i = j = k = 0
    
    # Copiar datos a las listas temporales
    while i < len(mitad_izquierda) and j < len(mitad_derecha):
      if mitad_izquierda[i] < mitad_derecha[j]:
        arr[k] = mitad_izquierda[i]
        i += 1
      else:
        arr[k] = mitad_derecha[j]
        j += 1
      k += 1
      
    # Comprobar si quedaron elementos
    while i < len(mitad_izquierda):
      arr[k] = mitad_izquierda[i]
      i += 1
      k += 1
      
    while j < len(mitad_derecha):
      arr[k] = mitad_derecha[j]
      j += 1
      k += 1
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"MergeSort: {merge_sort(lista.copy())}")