from abc import ABC, abstractmethod

#La clase abstracta tendra metodos abstractos, no se implementan
#Podemos definir comportamientos pero no son los que llevan a cabo estos comportamientos

class Figura(ABC):
    
    def __init__(self, lado=None, radio=None):
        self._lado = lado
        self._radio = radio
        if lado:
            print(f"abstract class initialized. lado={lado}")
        if radio:
            print(f"abstract class initialized. radio={radio}")
            
        super().__init__()
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

#No se pueden crear instancias de esta clase
#Solo de clases que desciendan de esta clase

class Cuadrado(Figura):
    
    #def __init__(self, lado) -> None:
    #    self._lado = lado
        
    def perimetro(self):
        return 4 * self._lado
    
    def area(self):
        return self._lado * self._lado
    
    
class Circulo(Figura):
    
    #def __init__(self, radio) -> None:
    #    self._radio = radio
        
    def perimetro(self):
        return 3.1416 * 2 * self._radio
    
    def area(self):
        return 3.1416 * self._radio ** 2
    
    
cuadrado = Cuadrado(lado=10)
print(cuadrado.area())
print(cuadrado.perimetro())

circulo = Circulo(radio=20)
print(circulo.area())
print(circulo.perimetro())