class Animal():
    
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    def __repr__(self) -> str:
        return (self._nombre)
        
animals = [Animal("Tigre"), Animal("Perro"), Animal("Gato")]

for index, animal in enumerate(animals):
    
    if animal._nombre == "Perro":
        animal._nombre = "Gaviota"
        break
    
print(animals)