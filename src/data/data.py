class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
      lista.reverse()
      return lista


    def buscar_elemento(self, lista, elemento):
       try:
            return lista.index(elemento)
       except ValueError:
            return -1
       
    def eliminar_duplicados(self, lista):
       if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista.")
       elementos_vistos = set()
       lista_sin_duplicados = []

       for elemento in lista:

            clave = (type(elemento), elemento)
            if clave not in elementos_vistos:
                elementos_vistos.add(clave)
                lista_sin_duplicados.append(elemento)

       return lista_sin_duplicados
    



    def merge_ordenado(self, lista1, lista2):
      return sorted(lista1 + lista2)
        
    
    def rotar_lista(self, lista, k):
       if not lista:
            return []
       k =  k % len(lista)
       return lista[-k:] + lista[:-k]


    def encuentra_numero_faltante(self, lista):
      n = len(lista) + 1
      return sum(range(1, n + 1)) - sum(lista)
    
    def es_subconjunto(self, conjunto1, conjunto2):
       return set(conjunto1).issubset(set(conjunto2))
     

    def implementar_pila(self):
       pila = []
       return {
        "push": pila.append,
        "pop": pila.pop,
        "peek": lambda: pila[-1] if pila else None,  
        "is_empty": lambda: len(pila) == 0  
    }
    
    def implementar_cola(self):
      from collections import deque
      cola = deque()
      return {
        "enqueue": cola.append,
        "dequeue": cola.popleft,
        "peek": lambda: cola[0] if cola else None,  
        "is_empty": lambda: len(cola) == 0  
    }
    
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [list(fila) for fila in zip(*matriz)]