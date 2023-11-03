class Animal():
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
        
    def hablar(self):
        print("Estoy hablando generico")
            
    def moverse(self):
        pass
    
    def correr():
        print("i am running")
    
    def describirme(self):
        print(f"Soy un animal de tipo {type(self).__name__}")
        
    def correr():
        print("Estoy corriendo")
        
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
   
        
dog = Perro('mamifero', 10)
dog.describirme()
print(dog.edad)
print(Perro.correr())
