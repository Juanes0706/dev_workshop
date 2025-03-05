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
    
    
    def es_numero_entero(self, cadena: str) -> bool:
        try:
            int(cadena)
            return True
        except ValueError:
            return False
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():
                desplazamiento_real = desplazamiento % 26
                codigo = ord('A') if caracter.isupper() else ord('a')
                resultado += chr((ord(caracter) - codigo + desplazamiento_real) % 26 + codigo)
            else:
                resultado += caracter
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        len_texto = len(texto)
        len_subcadena = len(subcadena)
        
        for i in range(len_texto - len_subcadena + 1):
            if texto[i:i + len_subcadena] == subcadena:
                posiciones.append(i)
        
        return posiciones