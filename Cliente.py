
class Cliente:
    
    def elegir_categoria(self):

        print("Bienvenido a la plataforma de streaming.")
        print("Por favor, elija una categoría:")
        print("1. Acción")
        print("2. Comedia")
        print("3. Terror")

        categoria_elegida = None
        while categoria_elegida not in [1, 2, 3]:
            try:
                categoria_elegida = int(input("> "))
                if categoria_elegida not in [1, 2, 3]:
                    print("Opción inválida. Por favor, elija una opción válida.")
            except ValueError:
                print("Opción inválida. Por favor, elija una opción válida.")

        if categoria.elegida == 1:
            categoria = 'Accion'()
        elif categoria.elegida == 2:
            categoria = 'Comedia'()
        elif categoria.elegida == 3:
            categoria = 'Terror'()

        print(categoria.mostrar_contenido())

        pelicula_elegida = None
        while pelicula_elegida not in ["Rapido y furioso", "The Love Pink", "The Conjuring"]:
            pelicula_elegida = input("Elija la película que desea ver: ")
            if pelicula_elegida not in ["John Wick", "The Hangover", "The Conjuring"]:
                print("Película no disponible. Por favor, elija una película disponible.")

pelicula = Peliculas(pelicula_elegida, categoria)
        
print(pelicula.mostrar_criterio())