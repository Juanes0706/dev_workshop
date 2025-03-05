class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a: bool, b: bool) -> bool:
        return a and b 
    
    def OR(self, a: bool, b: bool) -> bool:
        return a or b
    
    def NOT(self, a: bool) -> bool:
        return not a
    
    def XOR(self, a: bool, b: bool) -> bool:
        return a != b
    
    def NAND(self, a: bool, b: bool) -> bool:
        return not (a and b)
    
    def NOR(self, a: bool, b: bool) -> bool:
        return not (a or b)
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        pass
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        pass
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        pass
    
    
