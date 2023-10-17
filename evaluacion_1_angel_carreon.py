"""
Escriba una función que reciba 3 parámetros n1, n2, n3 y que retorne si es posible o no que se cumpla el Teorema de Pitágoras
"""

def evaluate_pitagoras(n1, n2, n3):
    
    """
    Se asume que n1 y n2 son los dos catetos del triangulo
    y el n3 es la hipotenusa.
    """
    
    #Primero valido que los 3 sean valores flotantes
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    
    #Despues valido que n1, n2 y n3 sean positivos y diferentes de 0, no pueden ser negativos
    if (n1 <= 0) or (n2 <= 0) or (n3 <= 0):
        print("No es posible que se cumpla el Teorema de pitágoras, todos los valores deben ser positivos y diferentes a 0")
        return False
    
    #Despues, valido que n3 sea mayor que n1 y que n2.
    if (n3 <= n1) or (n3 <= n2):
        print("No es posible que se cumpla el Teorema de pitágoras, n3 debe ser mayor que n1 y n2")
        return False

    #Despues Valida el Teorema de pitagoras, que establece que n3**2 = n1**2 + n2**2
    if n3**2 != (n1**2 + n2**2):
        print ("No es posible que se cumpla el Teorema de pitágoras, n3^2 no es igual a n1^2 + n2^2")
        return False
    
    print("Se cumple el teorema de pitágoras, n3^2 es igual a n1^2 + n2^2")
    return True
    
    
print(evaluate_pitagoras(1,2,3))
print(evaluate_pitagoras(1,-1,3))
print(evaluate_pitagoras(4,5,3))
print(evaluate_pitagoras(0,5,3))
print(evaluate_pitagoras(5,5,7))
print(evaluate_pitagoras(3,4,5))
print(evaluate_pitagoras("3", "4", 5))
    