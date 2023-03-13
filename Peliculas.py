class Peliculas():
    
    def _init_(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def mostrar_criterio(self):
        
        return 'La película {} está en la categoría {}'.forma(self.nombre, self.categoria)

criterios = Peliculas('The Love Pink')
print(criterios.mostrar_criterio())

