class NodoArbol:
  def __init__(self, clave):
    self.izquierda = None
    self.derecha = None
    self.val = clave

def insertar_en_arbol(raiz, clave):
  if raiz is None:
    return NodoArbol(clave)
  else:
    if clave < raiz.val:
      raiz.izquierda = insertar_en_arbol(raiz.izquierda, clave)
    else:
      raiz.derecha = insertar_en_arbol(raiz.derecha, clave)
  return raiz

def recorrido_en_orden(raiz, resultado):
  if raiz:
    recorrido_en_orden(raiz.izquierda, resultado)
    resultado.append(raiz.val)
    recorrido_en_orden(raiz.derecha, resultado)
  return resultado

def tree_sort(arr):
  if not arr:
    return []
  
  raiz = NodoArbol(arr[0])
  for i in range(1, len(arr)):
    insertar_en_arbol(raiz, arr[i])
    
  return recorrido_en_orden(raiz, [])

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(f"TreeSort: {tree_sort(lista.copy())}")