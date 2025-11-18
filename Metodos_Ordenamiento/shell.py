def shell_sort(arr):
  n = len(arr)
  # Empezar con un intervalo grande y reducirlo
  intervalo = n // 2
  while intervalo > 0:
    # Hacer un ordenamiento por inserción con este intervalo
    for i in range(intervalo, n):
      temp = arr[i]
      j = i
      while j >= intervalo and arr[j - intervalo] > temp:
        arr[j] = arr[j - intervalo]
        j -= intervalo
      arr[j] = temp
    intervalo //= 2 # Reducir el intervalo
  return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"ShellSort: {shell_sort(lista.copy())}")