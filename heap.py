import heapq

def heap_sort(arr):
  h = []
  # 1. Construir el montículo (heapq es un Min-Heap por defecto)
  for valor in arr:
    heapq.heappush(h, valor)
  
  # 2. Extraer los elementos en orden
  return [heapq.heappop(h) for i in range(len(h))]

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"HeapSort: {heap_sort(lista.copy())}")