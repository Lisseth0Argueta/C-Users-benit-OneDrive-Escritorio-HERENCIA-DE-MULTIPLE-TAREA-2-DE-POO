class Estudiantes:
    def __init__(self, nombre, apellido, carrera):
        self.nombre=nombre
        self.apellido=apellido
        self.carrera=carrera
        
    def registro(self):
        return 'La estudiante {} {} de carrera {}'.format(self.nombre, self.apellido, self.carrera)

Universidad= Estudiantes('Lisseth', 'Argueta', 'Ing. En desarrollo de software')
print(Universidad.registro())