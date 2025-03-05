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
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass