class Vehiculo():
    
    def __init__(self, motor, ruedas, color):
        self.motor = motor
        self.ruedas = ruedas
        self.color = color
    
    def __repr__(self) -> str:
        print("Soy un vehiculo de tipo " + type(self).__name__)
    #def avanzar(self):
    #    print("Avanzando...")
    
class Auto(Vehiculo):
    def __init__(self, motor, ruedas, color, puertas):
        super().__init__(motor, ruedas, color)
        self.puertas = puertas
    
class Camioneta(Auto):
    def __init__(self, motor, ruedas, color, puertas, caja):
        super().__init__(motor, ruedas, color, puertas)
        self.caja = caja

class Moto(Vehiculo):
    def __init__(self, motor, ruedas, color, tipo):
        super().__init__(motor, ruedas, color)
        self.tipo = tipo

class Cuatrimoto(Moto):
    def __init__(self, motor, ruedas, color, tipo, direccional):
        super().__init__(motor, ruedas, color, tipo)
        self.direccional = direccional
        
class Avion(Auto, Moto):
    def __init__(self, motor, ruedas, color, puertas, tipo, alas ):
        super().__init__(motor, ruedas, color, puertas, tipo)
        

Sentra = Auto("4 Cilindros", 4, "rojo", 5)
Frontier = Camioneta("6 Cilindros", 4, "blanco", 4, "Cubierta")
Italika = Moto("2 Cilindros", 2, "negra", "Basica")

Boeing = Avion("8 Cilindros", 2, "Blanco", 2, "737")