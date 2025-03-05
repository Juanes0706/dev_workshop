class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n: int) -> list:
        sequence = []
        for i in range(n):
            sequence.append(self.fibonacci(i))
        return sequence
    
    def es_primo(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n: int) -> list:
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n: int) -> bool:
        if n <= 1:
            return False
        suma_divisores = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma_divisores += i
                if i != n // i:
                    suma_divisores += n // i
        return suma_divisores == n
    
    def triangulo_pascal(self, filas: int) -> list:
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            if i > 1:
                for j in range(1, i):
                    fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n: int) -> int:
        return sum(int(d) for d in str(n))
    
    def es_numero_armstrong(self, n: int) -> bool:
        digitos = [int(d) for d in str(n)]
        longitud = len(digitos)
        suma = sum(d**longitud for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz: list) -> bool:
        n = len(matriz)
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        suma_objetivo = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_objetivo:
            return False
        return True
    
   