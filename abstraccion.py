#abstraccion
#Proceso en el cual se definen formalmente cuales son los atributos y
#los metodos dentro de una clase.

#Las clases que son abstractas no pueden ser instanciadas.
#Solo pueden ser llamadas entre clases.

from abc import ABC, abstractmethod

class myABC_Class(ABC):
    
    @abstractmethod #No puede ser instanciado
    def metodo_abstracto(self, x):
        return 45 + x

    def metodo_normal(self, x):
        return 58 + x
    
class myNormal_Class(myABC_Class):
    
    def metodo_abstracto(self, x):
        x = x+100
        return super().metodo_abstracto(x)
    
    def metodo_normal(self, x):
        return super().metodo_normal(x)
    
obj = myNormal_Class()
print(obj.metodo_abstracto(5))
print(obj.metodo_normal(10))