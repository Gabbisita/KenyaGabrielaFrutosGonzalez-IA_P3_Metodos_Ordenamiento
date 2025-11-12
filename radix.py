def counting_sort_for_radix(arr, exponente):
  n = len(arr)
  output = [0] * n
  count = [0] * 10 # Del 0 al 9

  # Contar ocurrencias de dígitos
  for i in range(n):
    indice = (arr[i] // exponente) % 10
    count[indice] += 1

  # Suma acumulativa
  for i in range(1, 10):
    count[i] += count[i - 1]

  # Construir el arreglo de salida
  i = n - 1
  while i >= 0:
    indice = (arr[i] // exponente) % 10
    output[count[indice] - 1] = arr[i]
    count[indice] -= 1
    i -= 1

  # Copiar el resultado
  for i in range(n):
    arr[i] = output[i]

def radix_sort(arr):
  # Encontrar el número máximo para saber el número de dígitos
  max_num = max(arr)
  
  # Hacer counting sort para cada dígito
  exponente = 1
  while max_num // exponente > 0:
    counting_sort_for_radix(arr, exponente)
    exponente *= 10
  return arr

# Ejemplo de uso
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"RadixSort: {radix_sort(lista.copy())}")