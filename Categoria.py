class Accion:
    
    def _init_(self):
        self.nombre = "Acción"

    def mostrar_contenido(self):
        return "Películas de acción disponibles: Rapido y furioso"


class Comedia:
    
    def _init_(self):
        self.nombre = "Comedia"

    def mostrar_contenido(self):
        return "Películas de comedia disponibles: The Love Pink"


class Terror:
    
    def _init_(self):
        self.nombre = "Terror"

    def mostrar_contenido(self):
        return "Películas de terror disponibles: The Conjuring"