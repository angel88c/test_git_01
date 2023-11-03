

class Alumno():
    
    estado = {
        1: "Activo",
        2: "Mora",
        3: "Retirado",
        4: "Egresado",
        5: "Certificado"
    }
    
    def __init__(self, nombre, apellido, mail):
        self._nombre = nombre
        self._apellido = apellido
        self._mail = mail
        self._estado = self.estado[2]
        

class Agenda():

    def __init__(self) -> None:
        self._lista_alumnos = []
        
    def agregar_alumno(self, nombre, apellido, mail):
        alumno = Alumno(nombre, apellido, mail)
        
        for student in self._lista_alumnos:
            if student.nombre == alumno._nombre:
                print(f"El alumno {student.nombre} ya existe.")
                return
            
        self._lista_alumnos.append(alumno)
        print("Nuevo alumno creado")
    
    def mostrar_todos_alumnos(self):
        
        print("Lista de alumnos:")
        for alumno, index in enumerate(self._lista_alumnos):
            print(f"{index+1}. nombre: {alumno.nombre}")
            print(f"{index+1}. nombre: {alumno.apellido}")
            print(f"{index+1}. nombre: {alumno.email}")
            print(f"{index+1}. nombre: {alumno.estado}")
            print("")
            
    def buscar_alumno(self, nombre_a_buscar):
        
        encontrado = False
        for alumno in self._lista_alumnos:
            if nombre_a_buscar == alumno.nombre:
                print(f"Alumno encontrado {nombre_a_buscar}")
                encontrado = True
                return alumno
            
        if not encontrado:
            print(f"Alumno no encontrado {nombre_a_buscar}")
            return None
    
    def buscar_por_estado(self, estado, modificar=False):
        
        alumnos_por_estado = []
        for alumno in self._lista_alumnos:
            if estado == alumno.estado:
                alumnos_por_estado.append(alumno)
            
        if alumnos_por_estado:
            print(f"{len(alumnos_por_estado)} Alumnos con estado {estado} encontrados.")
            for alumno, index in enumerate(alumnos_por_estado):
                print(f"{index+1}. nombre: {alumno.nombre}")
                print(f"{index+1}. nombre: {alumno.apellido}")
                print(f"{index+1}. nombre: {alumno.email}")
                print(f"{index+1}. nombre: {alumno.estado}")
                print("")


agenda = Agenda()
agenda.agregar_alumno("Mario", "Arias", "mario@123.com")
agenda.mostrar_todos_alumnos()