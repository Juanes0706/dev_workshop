class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, cadena: str) -> bool:
        cadena = ''.join(c for c in cadena if c.isalnum()).lower()
        return cadena == cadena[::-1]
    
    def invertir_cadena(self, cadena: str) -> str:
        return cadena[::-1]
    
    def contar_vocales(self, cadena: str) -> int:
        vocales = "aeiouAEIOU"
        return sum(1 for c in cadena if c in vocales)
    
    def contar_consonantes(self, cadena: str) -> int:
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for c in cadena if c in consonantes)
    
    def es_anagrama(self, cadena1: str, cadena2: str) -> bool:
        cadena1 = ''.join(c for c in cadena1 if c.isalnum()).lower()
        cadena2 = ''.join(c for c in cadena2 if c.isalnum()).lower()
        return sorted(cadena1) == sorted(cadena2)
    
    def contar_palabras(self, cadena: str) -> int:
        return len(cadena.split())
    
    def palabras_mayus(self, cadena: str) -> str:
        return ' '.join(word.capitalize() for word in cadena.split(' '))
    
    def eliminar_espacios_duplicados(self, cadena: str) -> str:
        return ' '.join(cadena.split())
    
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass